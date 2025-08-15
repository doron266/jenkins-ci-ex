
#!/usr/bin/env bash
set -e

cmd="${1:-}"
msg="${2:-demo change}"

case "$cmd" in
  up)
    docker compose up -d --build
    echo
    echo ">>> Jenkins: http://localhost:8080  (admin/admin123)"
    echo ">>> Job 'Demo-CI-Pipeline' points to ./demo-repo"
    ;;
  down)
    docker compose down -v
    ;;
  commit)
    (cd demo-repo &&       git config user.email "demo@example.com" &&       git config user.name "Demo User" &&       echo "# $msg" >> README.md &&       git add README.md && git commit -m "$msg")
    echo "Committed. Jenkins polls SCM every minute or click 'Build Now'."
    ;;
  logs)
    docker logs -f jenkins-ci-demo
    ;;
  *)
    echo "Usage: ./demo.sh {up|down|commit|logs} [message]"
    ;;
esac
