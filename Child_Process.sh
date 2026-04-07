#!/bin/bash

echo "Parent PID: $$"
(
 echo "Inside child process..."
 echo "Child PID: $BASHPID"
 sleep 3
)
