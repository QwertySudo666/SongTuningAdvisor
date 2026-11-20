FROM ubuntu:latest
LABEL authors="darkbrother"

ENTRYPOINT ["top", "-b"]