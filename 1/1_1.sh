#!/bin/sh
awk 'function f(){m=(n>m)?n:m;n=0}/./{n+=$1}/^$/{f()}END{f();print m}' <input
