#!/bin/bash

echo "** Running PyFlakes **"

cd apps
pyflakes photo_manager
pyflakes administrator
