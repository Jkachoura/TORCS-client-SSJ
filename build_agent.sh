#!/usr/bin/env bash
# Author: J.A.Boogaard@hr.nl

repo="ghcr.io/alxcnl"
image_name="torcs-agent"
group="02"
tag="30${group}"
image="${repo}/${image_name}:${tag}"
dockerfile="Dockerfile" 
arch=$(uname -m)

if [[ -n $1 ]]; then
    action=$1
else
    action="load"
fi

if [[ "$action" -eq "push" ]]; then
    cmd="docker buildx build --${action} --build-arg PLATFORM=amd64,arm64 -f ${dockerfile} -t $image ."
    echo $cmd
    eval $cmd

fi