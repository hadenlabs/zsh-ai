#!/usr/bin/env ksh
# -*- coding: utf-8 -*-

function ai::internal::opencode::load {
    [ -e "${AI_OPENCODE_BIN_PATH}" ] && export PATH="${AI_OPENCODE_BIN_PATH}:${PATH}"
}

function ai::internal::packages::install {
    message_info "Installing required ai packages"
    for package in "${AI_PACKAGES[@]}"; do
        case "${package}" in
            opencode)
                ai::internal::opencode::install
                ;;
            fabric)
                ai::internal::fabric::install
                ;;
            ollama)
                ai::internal::ollama::install
                ;;
            *)
                core::install "${package}"
                ;;
        esac
    done
    message_success "Installed required ai packages"
}

function ai::internal::opencode::install {
    if core::exists opencode; then
        return 0
    fi

    message_info "Installing opencode..."
    if curl -fsSL "${AI_INSTALL_URL_OPENCODE}" | bash; then
        message_success "opencode installed successfully"
    else
        message_error "Failed to install opencode"
        return 1
    fi
}

function ai::internal::fabric::install {
    if core::exists fabric; then
        return 0
    fi

    message_info "Installing fabric..."
    if curl -fsSL "${AI_INSTALL_URL_FABRIC}" | bash; then
        message_success "fabric installed successfully"
    else
        message_error "Failed to install fabric"
        return 1
    fi
}

function ai::internal::fabric::patterns::sync {
    if [[ ! -d "${AI_FABRIC_PATTERNS_SYNC_SOURCE}" ]]; then
        message_warning "Patterns source directory not found: ${AI_FABRIC_PATTERNS_SYNC_SOURCE}"
        return 1
    fi

    message_info "Syncing patterns from ${AI_FABRIC_PATTERNS_SYNC_SOURCE} to ${AI_FABRIC_PATTERNS_PATH}..."

    mkdir -p "${AI_FABRIC_PATTERNS_PATH}"

    if rsync -av --delete "${AI_FABRIC_PATTERNS_SYNC_SOURCE}/" "${AI_FABRIC_PATTERNS_PATH}/"; then
        message_success "Patterns synced successfully"
    else
        message_error "Failed to sync patterns"
        return 1
    fi
}

function ai::internal::fabric::patterns::pull {
    if core::exists fabric; then
        message_info "Updating fabric patterns..."
        fabric --updatepatterns
        message_success "Patterns updated"
    else
        message_error "fabric is not installed"
        return 1
    fi
}

function ai::internal::ollama::install {
    if core::exists ollama; then
        return 0
    fi

    message_info "Installing ollama..."
    if curl -fsSL "${AI_INSTALL_URL_OLLAMA}" | sh; then
        message_success "ollama installed successfully"
    else
        message_error "Failed to install ollama"
        return 1
    fi
}

function ai::internal::ollama::models::list {
    if ! core::exists ollama; then
        message_error "ollama is not installed"
        return 1
    fi

    message_info "Listing ollama models..."
    ollama list
}

function ai::internal::ollama::models::pull {
    if ! core::exists ollama; then
        message_error "ollama is not installed"
        return 1
    fi

    local model="${1}"
    if [[ -z "${model}" ]]; then
        message_error "Model name required: ai::ollama::models::pull <model>"
        return 1
    fi

    message_info "Pulling model: ${model}..."
    ollama pull "${model}"
}

function ai::internal::ollama::models::install {
    if ! core::exists ollama; then
        message_error "ollama is not installed"
        return 1
    fi

    message_info "Installing default ollama models..."
    for model in "${AI_OLLAMA_MODELS[@]}"; do
        message_info "Pulling model: ${model}..."
        ollama pull "${model}"
    done
    message_success "All default models installed"
}
