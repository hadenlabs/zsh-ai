#!/usr/bin/env ksh
# -*- coding: utf-8 -*-

function ai::internal::packages::install {
    message_info "Installing required ai packages"
    for package in "${AI_PACKAGES[@]}"; do
        core::install "${package}"
    done
    message_success "Installed required ai packages"
}
