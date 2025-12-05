#!/bin/bash
# =============================================================================
# Clone Third-Party Dependencies Script
# =============================================================================
#
# This script clones Git repositories listed in a dependencies file (by default
# oca_dependencies.txt). These dependencies are required for testing and running
# Odoo addons that depend on modules from external repositories.
#
# USAGE:
#   ./clone_dependencies.sh [OPTIONS]
#
# OPTIONS:
#   --branch <branch>    Odoo version branch to clone (e.g., 13.0, 14.0, 16.0)
#                        If not specified, defaults to "13.0"
#   --deps-dir <dir>     Directory to clone dependencies into
#                        Defaults to ${HOME}/dependencies
#   --deps-file <file>   Path to dependencies file
#                        Defaults to oca_dependencies.txt
#
# ENVIRONMENT VARIABLES:
#   ADDONS_PATH          If set, cloned paths will be appended to this
#   GITHUB_ENV           If set (in GitHub Actions), ADDONS_PATH is exported
#
# FILE FORMAT (oca_dependencies.txt):
#   Each line should contain:
#     repo_name [custom_url] [custom_branch]
#
#   - repo_name: Repository name (e.g., credit-control, bank-payment)
#   - custom_url: Optional Git URL (defaults to https://github.com/OCA/{repo_name}.git)
#   - custom_branch: Optional branch override (defaults to --branch value)
#   - Lines starting with # are treated as comments
#   - Empty lines are ignored
#
#   Example oca_dependencies.txt:
#     # OCA repositories (URL defaults to https://github.com/OCA/{name}.git)
#     credit-control
#     bank-payment
#     brand
#
#     # Custom repository with explicit URL
#     my-repo https://github.com/myorg/my-repo.git
#
#     # Repository with custom URL and specific branch
#     custom-addons https://github.com/user/custom-addons.git 14.0
#
# SCRIPT EXAMPLES:
#   # Clone dependencies for Odoo 14.0
#   ./clone_dependencies.sh --branch 14.0
#
#   # Clone to a custom directory
#   ./clone_dependencies.sh --deps-dir /opt/deps
#
#   # Use with custom dependencies file
#   ./clone_dependencies.sh --deps-file my_deps.txt --branch 16.0
#
# =============================================================================

set -e

# Default values
DEFAULT_BRANCH="13.0"
DEPS_DIR="${HOME}/dependencies"
DEPS_FILE="oca_dependencies.txt"
BRANCH=""

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --branch)
            BRANCH="$2"
            shift 2
            ;;
        --deps-dir)
            DEPS_DIR="$2"
            shift 2
            ;;
        --deps-file)
            DEPS_FILE="$2"
            shift 2
            ;;
        -h|--help)
            head -56 "$0" | tail -n +2 | sed 's/^# //' | sed 's/^#//'
            exit 0
            ;;
        *)
            echo "::error::Unknown option: $1"
            exit 1
            ;;
    esac
done

# Use default branch if not specified
if [ -z "$BRANCH" ]; then
    BRANCH="$DEFAULT_BRANCH"
fi

echo "========================================"
echo "Clone Third-Party Dependencies"
echo "========================================"
echo "Dependencies file: ${DEPS_FILE}"
echo "Target directory: ${DEPS_DIR}"
echo "Default branch: ${BRANCH}"
echo "========================================"

# Check if dependencies file exists
if [ ! -f "$DEPS_FILE" ]; then
    echo "::warning::Dependencies file not found: ${DEPS_FILE}"
    echo "No dependencies to clone."
    exit 0
fi

# Create dependencies directory
mkdir -p "${DEPS_DIR}"

# Track clone status
clone_failed=0
clone_count=0

# Read and process dependencies file
# Note: The "|| [ -n "$line" ]" ensures the last line is processed even if the file doesn't end with a newline
while IFS= read -r line || [ -n "$line" ]; do
    # Skip comments and empty lines
    line=$(echo "$line" | sed 's/#.*//' | xargs)
    [ -z "$line" ] && continue

    # Parse line: repo_name [url] [branch]
    repo_name=$(echo "$line" | awk '{print $1}')
    repo_url=$(echo "$line" | awk '{print $2}')
    repo_branch=$(echo "$line" | awk '{print $3}')

    # Default to OCA GitHub URL if no custom URL is specified
    if [ -z "$repo_url" ]; then
        repo_url="https://github.com/OCA/${repo_name}.git"
    fi

    # Default to specified branch if not overridden
    if [ -z "$repo_branch" ]; then
        repo_branch="${BRANCH}"
    fi

    echo ""
    echo "----------------------------------------"
    echo "Cloning: ${repo_name}"
    echo "  URL: ${repo_url}"
    echo "  Branch: ${repo_branch}"
    echo "  Target: ${DEPS_DIR}/${repo_name}"
    echo "----------------------------------------"

    if git clone --depth 1 --branch "${repo_branch}" "${repo_url}" "${DEPS_DIR}/${repo_name}"; then
        echo "✓ Successfully cloned ${repo_name}"
        clone_count=$((clone_count + 1))
    else
        echo "::error::Failed to clone ${repo_name} from ${repo_url}"
        clone_failed=1
    fi
done < "$DEPS_FILE"

echo ""
echo "========================================"
echo "Clone Summary"
echo "========================================"
echo "Total cloned: ${clone_count}"

if [ "$clone_failed" -eq 1 ]; then
    echo "::error::One or more dependencies failed to clone"
    exit 1
fi

# Build ADDONS_PATH from cloned dependencies
DEPS_ADDONS_PATH=""
if [ -d "${DEPS_DIR}" ]; then
    # Check if directory has subdirectories
    if find "${DEPS_DIR}" -mindepth 1 -maxdepth 1 -type d -print -quit 2>/dev/null | grep -q .; then
        for dir in ${DEPS_DIR}/*/; do
            if [ -d "$dir" ]; then
                # Remove trailing slash for cleaner paths
                dir="${dir%/}"
                if [ -z "$DEPS_ADDONS_PATH" ]; then
                    DEPS_ADDONS_PATH="${dir}"
                else
                    DEPS_ADDONS_PATH="${DEPS_ADDONS_PATH},${dir}"
                fi
            fi
        done
    fi
fi

# Export ADDONS_PATH if running in GitHub Actions
if [ -n "$DEPS_ADDONS_PATH" ]; then
    echo ""
    echo "Dependencies added to ADDONS_PATH:"
    echo "$DEPS_ADDONS_PATH" | tr ',' '\n' | sed 's/^/  - /'
    
    if [ -n "$GITHUB_ENV" ]; then
        if [ -n "$ADDONS_PATH" ]; then
            echo "ADDONS_PATH=${ADDONS_PATH},${DEPS_ADDONS_PATH}" >> "$GITHUB_ENV"
        else
            echo "ADDONS_PATH=${DEPS_ADDONS_PATH}" >> "$GITHUB_ENV"
        fi
        echo ""
        echo "ADDONS_PATH exported to GitHub environment."
    fi
fi

echo ""
echo "✓ All dependencies cloned successfully!"
