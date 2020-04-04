#!/bin/sh

alembic downgrade base
rm -rf migrations/versions/*
alembic revision --autogenerate -m "initial db page"
alembic upgrade head
