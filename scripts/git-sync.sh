#!/bin/bash
# Interactive helper to sync Dalco repos (core, apps, dev_tools)

# Base path = parent of scripts folder
BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

REPOS=("dalco_core" "dalco_applications" "dalco_dev_tools")

echo "Select a repository to work with:"
select repo in "${REPOS[@]}" "all"; do
  case $repo in
    dalco_core|dalco_applications|dalco_dev_tools|all)
      TARGET=$repo
      break
      ;;
    *)
      echo "Invalid choice, try again."
      ;;
  esac
done

echo ""
echo "Select an action:"
select action in "pull" "push" "status"; do
  case $action in
    pull|push|status)
      ACTION=$action
      break
      ;;
    *)
      echo "Invalid choice, try again."
      ;;
  esac
done

if [ "$ACTION" = "push" ]; then
  echo ""
  read -p "Enter commit message (leave empty for auto message): " COMMIT_MSG
  if [ -z "$COMMIT_MSG" ]; then
    COMMIT_MSG="Update from $(hostname) at $(date '+%Y-%m-%d %H:%M:%S')"
  fi
fi

# Determine which repos to process
if [ "$TARGET" = "all" ]; then
  SELECTED_REPOS=("${REPOS[@]}")
else
  SELECTED_REPOS=("$TARGET")
fi

# Loop through repos
for repo in "${SELECTED_REPOS[@]}"; do
  if [ "$repo" = "dalco_dev_tools" ]; then
    REPO_PATH="$BASE_DIR"
  else
    REPO_PATH="$BASE_DIR/../$repo"
  fi

  if [ -d "$REPO_PATH/.git" ]; then
    echo ""
    echo ">>> Working on $repo ($ACTION)"
    cd "$REPO_PATH" || exit
    case $ACTION in
      pull)
        git pull
        ;;
      push)
        git add .
        git commit -m "$COMMIT_MSG" || true
        git push
        ;;
      status)
        git status -s
        ;;
    esac
    cd - >/dev/null || exit
  else
    echo "Skipping $repo (not a git repo at $REPO_PATH)"
  fi
done
