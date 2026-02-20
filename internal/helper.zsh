#!/usr/bin/env ksh
# -*- coding: utf-8 -*-

function ai::internal::opencode::install {
    if which opencode &> /dev/null; then
        message_info "opencode is already installed"
        return 0
    fi

    message_info "Installing opencode..."
    if curl -fsSL https://opencode.ai/install | bash; then
        message_success "opencode installed successfully"
    else
        message_error "Failed to install opencode"
        return 1
    fi
}
