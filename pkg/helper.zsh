#!/usr/bin/env ksh
# -*- coding: utf-8 -*-

function ai::opencode::install {
    ai::internal::opencode::install
}

function ai::fabric::install {
    ai::internal::fabric::install
}

function ai::fabric::patterns::sync {
    ai::internal::fabric::patterns::sync
}

function ai::fabric::patterns::pull {
    ai::internal::fabric::patterns::pull
}

function ai::ollama::install {
    ai::internal::ollama::install
}

function ai::ollama::models::list {
    ai::internal::ollama::models::list
}

function ai::ollama::models::pull {
    ai::internal::ollama::models::pull "${@}"
}
