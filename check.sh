#!/bin/sh
# Compiles every step of every lesson in python:3.12-slim: the check each lesson passed before its video went out.
# Needs Docker. A step folder holding .nocheck does not compile on purpose and is skipped.
docker run --rm --entrypoint /bin/sh -v "$PWD:/w" python:3.12-slim -c '
pip install -q --disable-pip-version-check --root-user-action=ignore mypy==1.13.0 >/dev/null 2>&1
cd /w; fail=0
for f in */step-*/*.py; do
  [ -e "$f" ] || continue
  [ -e "$(dirname "$f")/.nocheck" ] && continue
  d=$(mktemp -d)
  if ( mypy --no-error-summary --check-untyped-defs $f ) >/tmp/log 2>&1; then echo "ok    $f"; else echo "FAIL  $f"; cat /tmp/log; fail=1; fi
done
exit $fail'
