# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

setopt correct                                                  # Auto correct mistakes
setopt extendedglob                                             # Extended globbing. Allows using regular expressions with *
setopt nocaseglob                                               # Case insensitive globbing
setopt rcexpandparam                                            # Array expension with parameters
setopt nocheckjobs                                              # Don't warn about running processes when exiting
setopt numericglobsort                                          # Sort filenames numerically when it makes sense
setopt nobeep                                                   # No beep
setopt appendhistory                                            # Immediately append history instead of overwriting
setopt histignorealldups                                        # If a new command is a duplicate, remove the older one
setopt inc_append_history                                       # save commands are added to the history immediately, otherwise only when shell exits.
setopt histignorespace                                          # Don't save commands that start with space

zstyle ':completion:*' matcher-list 'm:{a-zA-Z}={A-Za-z}'       # Case insensitive tab completion
zstyle ':completion:*' list-colors "${(s.:.)LS_COLORS}"         # Colored completion (different colors for dirs/files/etc)
zstyle ':completion:*' rehash true                              # automatically find new executables in path
# Speed up completions
zstyle ':completion:*' accept-exact '*(N)'
zstyle ':completion:*' use-cache on
zstyle ':completion:*' cache-path ~/.zsh/cache
HISTFILE=~/.zhistory
HISTSIZE=10000
SAVEHIST=10000
WORDCHARS=${WORDCHARS//\/[&.;]}                                 # Don't consider certain characters part of the word

# Exports
export PATH="${PATH}:/opt/depot_tools:/home/til/.local/share/gem/ruby/3.0.0/bin:/home/til/.local/bin"
export GPG_TTY=$TTY
export EDITOR=nvim
export VISUAL=nvim
export DIFFPROG=nvimdiff
export BROWSER=qutebrowser
export DEPOT_TOOLS_UPDATE=0

XDG_CACHE_HOME=$HOME/.cache
XDG_CONFIG_HOME=$HOME/.config
XDG_DATA_HOME=$HOME/.local/share
XDG_STATE_HOME=$HOME/.local/state

# Alias section

# Confirm before overwriting something
alias cp="cp -i"
alias mv='mv -i'
alias rm='rm -I'

alias df='df -h'                                                # Human-readable sizes
alias free='free -m'                                            # Show sizes in MB

# git aliases
alias gitu='git add . && git commit && git push'
alias ga="git add"
alias gd="git diff"
alias gs="git status"
alias gl="git lg"
alias gc="git commit"
alias gsw="git switch"

alias n="nvim"

alias zathura='zathura --fork'

alias man='batman'

# Use eza instead of ls

# Exit if the 'eza' command could not be found
if ! (( $+commands[eza] )); then
    echo "ERROR: 'eza' command not found"
    return
fi

# Create alias override commands using 'eza'
alias ls='eza --group-directories-first --icons'
alias ll='ls -lbh --git --git-repos'
alias la='ll -a'
alias tree='ll --tree --level=2'


# python venvs

export VENV_HOME="$HOME/.virtualenvs"
[[ -d $VENV_HOME ]] || mkdir $VENV_HOME

lsvenv() {
    ls -1 $VENV_HOME
}

venv() {
    if [ $# -eq 0 ]
        then
            echo "Please provide venv name"
        else
            source "$VENV_HOME/$1/bin/activate"
    fi
}

mkvenv() {
    if [ $# -eq 0 ]
        then
            echo "Please provide venv name"
        else
            python3 -m venv $VENV_HOME/$1
    fi
}

rmvenv() {
    if [ $# -eq 0 ]
        then
            echo "Please provide venv name"
        else
            rm -r $VENV_HOME/$1
    fi
}


# Plugins
source /usr/share/zsh/share/antigen.zsh
antigen bundle zsh-users/zsh-autosuggestions
antigen bundle zsh-users/zsh-syntax-highlighting
antigen bundle zap-zsh/vim
antigen bundle zsh-users/zsh-history-substring-search
antigen bundle zsh-users/zsh-completions
antigen bundle hlissner/zsh-autopair
antigen theme romkatv/powerlevel10k
antigen apply

bindkey '^[[A' history-substring-search-up
bindkey '^[[B' history-substring-search-down

