#!/bin/bash

# Run a docker-compose command configured with the project and environment
function d-c() {
    project=$(basename $(pwd))
    docker-compose -p ${project} -f etc/compose-dev.yml "$@"
}

case "$1" in
    "django")
        d-c exec django ./manage.py ${@:2}
        ;;

    "fmt")
        d-c exec django black .
        ;;

    "logs")
        shift
        d-c logs -f "$@"
        ;;

    "test")
        shift
        d-c exec django pytest --cov --no-cov-on-fail --cov-report=html --cov-branch --nomigrations "$@"
        ;;

    "run")
        d-c stop -t 0
        d-c build
        d-c up -d
        ;;
esac
