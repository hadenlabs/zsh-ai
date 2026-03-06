#!/usr/bin/env ksh
# -*- coding: utf-8 -*-

function ai::internal::opencode::load {
    [ -e "${AI_OPENCODE_BIN_PATH}" ] && export PATH="${AI_OPENCODE_BIN_PATH}:${PATH}"
}

function ai::internal::shimmy::load {
    [ -e "${AI_SHIMMY_BIN_PATH}" ] && export PATH="${AI_SHIMMY_BIN_PATH}:${PATH}"
}

function ai::internal::openclaw::load {
    [ -e "${AI_OPENCLAW_BIN_PATH}" ] && export PATH="${AI_OPENCLAW_BIN_PATH}:${PATH}"
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
            shimmy)
                ai::internal::shimmy::install
                ;;
            hf)
                ai::internal::hf::install
                ;;
            openclaw)
                ai::internal::openclaw::install
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

function ai::internal::opencode::sync {
    if ! core::exists rsync; then
        message_error "rsync is not installed"
        return 1
    fi

    message_info "Syncing opencode config from ${AI_OPENCODE_CONFIG_SOURCE_PATH} to ${AI_OPENCODE_CONFIG_PATH}..."

    mkdir -p "${AI_OPENCODE_CONFIG_PATH}"

    if rsync -av "${AI_OPENCODE_CONFIG_SOURCE_PATH}/" "${AI_OPENCODE_CONFIG_PATH}/"; then
        message_success "opencode config synced successfully"
    else
        message_error "Failed to sync opencode config"
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

function ai::internal::shimmy::install {
    if core::exists shimmy; then
        return 0
    fi

    mkdir -p "${AI_SHIMMY_BIN_PATH}"

    if curl -fsSL "${AI_INSTALL_URL_SHIMMY}" -o "${AI_SHIMMY_BIN_PATH}/shimmy"; then
        chmod +x "${AI_SHIMMY_BIN_PATH}/shimmy"
        message_success "shimmy installed successfully"
    else
        message_error "Failed to install shimmy"
        return 1
    fi
}

function ai::internal::hf::install {
    if core::exists hf; then
        return 0
    fi

    message_info "Installing hf CLI..."
    if curl -fsSL "${AI_INSTALL_URL_HF}" | bash; then
        message_success "hf installed successfully"
    else
        message_error "Failed to install hf"
        return 1
    fi
}

function ai::internal::openclaw::install {
    if core::exists openclaw; then
        return 0
    fi

    mkdir -p "${AI_OPENCLAW_BIN_PATH}"

    message_info "Installing openclaw..."

    if curl -fsSL "${AI_INSTALL_URL_OPENCLAW}" | bash; then
        message_success "openclaw installed successfully"
    else
        message_error "Failed to install openclaw"
        return 1
    fi
}
