"
" dotvim : https://github.com/dotphiles/dotvim
"
" Setup vim and load required plugins before dotvim
"
" Authors:
"   Ben O'Hara <bohara@gmail.com>
"

" Call dotvim
source ~/.vim/dotvim.vim

if has("user_commands")
  set nocompatible
  filetype off
  set rtp+=~/.vim/bundle/vundle/
  call vundle#rc()
  "let g:vundles=['general', 'git', 'hg', 'programming', 'completion', 'ruby', 'python', 'misc']
  "let g:vundles=['general', 'python', 'programming', 'git']
  let g:vundles=['general', 'programming', 'php', 'ruby', 'python', 'javascript', 'html', 'misc']

  "let g:neocomplcache_enable_at_startup = 1
  " Load 'vundles'
  source ~/.vim/vundles.vim
  " Add extra bundles here...
  " Bundle 'reponame'
  let g:dotvim_colorscheme = 'Monokai'

  Plugin 'vim-airline/vim-airline-themes'
endif

" Override colorscheme from base16
Plugin 'flazz/vim-colorschemes'

" Customize to your needs...

