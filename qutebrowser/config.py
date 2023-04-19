## This is here so configs done via the GUI are still loaded.
## Remove it to not load settings done via the GUI.
config.load_autoconfig(True)

# Search engines
c.url.searchengines.update({
    'DEFAULT':  'https://www.google.de/search?q={}',
    'gg':       'https://www.google.de/search?q={}',
    'duck':     'https://duckduckgo.com/?q={}&ia=web',
    'eco':      'https://www.ecosia.org/search?q={}',
    'map':      'https://www.google.com/maps/place/{}',
    'arch':     'https://wiki.archlinux.org/index.php?search={}',
    'clang':    'https://duckduckgo.com/?q=\\site:clang.llvm.org/doxygen+{}',
    'llvm':     'https://duckduckgo.com/?q=\\site:llvm.org/doxygen+{}',
    'aio':      'http://www.aiosearch.com/search/4/Torrents/{}/',
    'we':     'https://en.wikipedia.org/w/index.php?search={}&fulltext=1',
    'wd':       'https://de.wikipedia.org/wiki/{}',
    'cpp':      'http://en.cppreference.com/mwiki/index.php?search={}',
    'amazon':   'https://smile.amazon.de/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords={}',
    'dblp':     'https://dblp.uni-trier.de/search?q={}',
    'acm':      'https://dl.acm.org/results.cfm?query={}',
    'gs':       'https://scholar.google.de/scholar?q={}',
    'steamdb':  'https://steamdb.info/search/?a=app&q={}',
    'dict':     'https://www.dict.cc/?s={}',
    'leo':      'https://dict.leo.org/german-english/{}',
    'ling':     'https://www.linguee.com/english-german/search?source=auto&query={}',
    'yt':       'https://www.youtube.com/results?search_query={}',
    'wolfram':  'https://www.wolframalpha.com/input/?i={}',
    'py':       'https://docs.python.org/3/search.html?q={}&check_keywords=yes',
    'nzb':      'https://www.binsearch.info/?q={}&max=250&adv_age=1100&server=',
    'ghub':     'https://github.com/search?q={}',
    'hy':       'https://www.hyphenation24.com/word/{}/',
    'dhl':      'https://www.dhl.de/en/privatkunden/pakete-empfangen/verfolgen.html?piececode={}',
    'duden':    'https://www.duden.de/suchen/dudenonline/{}',
    'fa':       'https://fontawesome.com/search?q={}&o=r',
    'intrin':   'https://software.intel.com/sites/landingpage/IntrinsicsGuide/#text={}',
    'stock':    'https://www.finanzen.net/suchergebnis.asp?_search={}',
    'tex':      'https://duckduckgo.com/?q=\\site:www.weinelt.de/latex/+{}',
})

## Aliases for commands. The keys of the given dictionary are the
## aliases, while the values are the commands they map to.
## Type: Dict
c.aliases = {
    'w': 'session-save',
    'l': 'session-load',
    'q': 'close',
    'qa': 'quit',
    'wq': 'quit --save',
    'wqa': 'quit --save'
}

# SSL/TLS Certificate Error Handling
c.content.tls.certificate_errors = 'ask-block-thirdparty' # ask for page loads with errors, automatically block resource loads

## Which pages to apply dark mode to. The underlying Chromium setting has
## been removed in QtWebEngine 5.15.3, thus this setting is ignored
## there. Instead, every element is now classified individually.
## Type: String
## Valid values:
##   - always: Apply dark mode filter to all frames, regardless of content.
##   - smart: Apply dark mode filter to frames based on background color.
c.colors.webpage.darkmode.policy.page = 'always'

## Value to use for `prefers-color-scheme:` for websites. The "light"
## value is only available with QtWebEngine 5.15.2+. On older versions,
## it is the same as "auto". The "auto" value is broken on QtWebEngine
## 5.15.2 due to a Qt bug. There, it will fall back to "light"
## unconditionally.
## Type: String
## Valid values:
##   - auto: Use the system-wide color scheme setting.
##   - light: Force a light theme.
##   - dark: Force a dark theme.
c.colors.webpage.preferred_color_scheme = 'dark'

## Enable the ad/host blocker
## Type: Bool
c.content.blocking.enabled = True

## Block subdomains of blocked hosts. Note: If only a single subdomain is
## blocked but should be allowed, consider using
## `content.blocking.whitelist` instead.
## Type: Bool
#  c.content.blocking.hosts.block_subdomains = True

## Which method of blocking ads should be used.  Support for Adblock Plus
## (ABP) syntax blocklists using Brave's Rust library requires the
## `adblock` Python package to be installed, which is an optional
## dependency of qutebrowser. It is required when either `adblock` or
## `both` are selected.
## Type: String
## Valid values:
##   - auto: Use Brave's ABP-style adblocker if available, host blocking otherwise
##   - adblock: Use Brave's ABP-style adblocker
##   - hosts: Use hosts blocking
##   - both: Use both hosts blocking and Brave's ABP-style adblocker
c.content.blocking.method = 'both'
