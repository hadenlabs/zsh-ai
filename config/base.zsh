#!/usr/bin/env ksh
# -*- coding: utf-8 -*-

export AI_MESSAGE_BREW="Please install brew or use antibody bundle luismayta/zsh-brew"
export AI_PACKAGE_NAME=ai

# opencode

export AI_OPENCODE_ROOT_PATH="${HOME}/.opencode"
export AI_OPENCODE_BIN_PATH="${AI_OPENCODE_ROOT_PATH}/bin"

# fabric

export AI_FABRIC_PATTERNS_PATH="${HOME}/.config/fabric/patterns"
export AI_FABRIC_PATTERNS_SYNC_SOURCE="${ZSH_AI_PATH}/patterns"

# ollama

export AI_OLLAMA_MODELS_PATH="${HOME}/.ollama/models"

# installation urls

export AI_INSTALL_URL_OPENCODE="https://opencode.ai/install"
export AI_INSTALL_URL_FABRIC="https://raw.githubusercontent.com/danielmiessler/fabric/main/scripts/installer/install.sh"
export AI_INSTALL_URL_OLLAMA="https://ollama.com/install.sh"

export AI_TOOLS=(
  opencode
  fabric
  ollama
)

export AI_PACKAGES=(
    "${AI_TOOLS[@]}"
)
