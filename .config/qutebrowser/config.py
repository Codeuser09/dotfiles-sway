import sys
import os.path

secretsExists = False
secretFile = os.path.expanduser("~/.config/qutebrowser/qutesecrets.py")

if os.path.isfile(secretFile):
    sys.path.append(os.path.dirname(secretFile))
    import qutesecrets

    secretsExists = True

config.set("scrolling.smooth", True)
config.set(
    "qt.args",
    [
        "ignore-gpu-blacklist",
        "enable-gpu-rasterization",
        "enable-native-gpu-memory-buffers",
        "num-raster-threads=4",
    ],
)
config.load_autoconfig(True)

# Catppuccin Frappé color palette
base00 = "#303446"
base01 = "#292c3c"
base02 = "#414559"
base03 = "#51576d"
base04 = "#626880"
base05 = "#c6d0f5"
base06 = "#f2d5cf"
base07 = "#babbf1"
base08 = "#e78284"
base09 = "#ef9f76"
base0A = "#e5c890"
base0B = "#a6d189"
base0C = "#81c8be"
base0D = "#8caaee"
base0E = "#ca9ee6"
base0F = "#eebebe"

config.set("content.cookies.accept", "no-3rdparty", "chrome-devtools://*")
config.set("content.cookies.accept", "no-3rdparty", "devtools://*")

config.set(
    "content.headers.user_agent",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
)
config.set(
    "content.headers.user_agent",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "https://accounts.google.com/*",
)
config.set(
    "content.headers.user_agent",
    "Mozilla/5.0 ({os_info}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99 Safari/537.36",
    "https://*.slack.com/*",
)

config.set("content.images", True, "chrome-devtools://*")
config.set("content.images", True, "devtools://*")

config.set("content.javascript.enabled", True, "chrome-devtools://*")
config.set("content.javascript.enabled", True, "devtools://*")
config.set("content.javascript.enabled", True, "chrome://*/*")
config.set("content.javascript.enabled", True, "qute://*/*")

config.set("content.javascript.enabled", True, "qute://*/*")

c.tabs.favicons.scale = 3
c.tabs.last_close = "close"
c.tabs.position = "left"
c.tabs.width = "3%"
c.tabs.padding = {"left": 0, "right": 0, "top": 10, "bottom": 10}
c.tabs.title.format = "{index}"
c.window.transparent = True
c.colors.webpage.darkmode.enabled = True

c.colors.webpage.preferred_color_scheme = "dark"
c.colors.webpage.darkmode.policy.images = "never"

c.url.default_page = str(config.configdir) + "/qute-home.html"
c.url.start_pages = str(config.configdir) + "/qute-home.html"

c.url.searchengines = {
    "DEFAULT": "https://startpage.com/do/search?query={}",
    "d": "https://duckduckgo.com/?q={}&ia=web",
    "az": "https://www.amazon.com/s?k={}",
    "aw": "https://wiki.archlinux.org/index.php?search={}&title=Special%3ASearch&wprov=acrw1",
    "nw": "https://nixos.wiki/index.php?search={}&go=Go",
    "mn": "https://mynixos.com/search?q={}",
    "sb": "https://www.serebii.net/search.shtml?q={}&sa=Search",
    "bp": "https://bulbapedia.bulbagarden.net/wiki/index.php?title=Special%3ASearch&search={}&go=Go",
    "yt": "https://www.youtube.com/results?search_query={}",
    "od": "https://odysee.com/$/search?q={}",
    "gd": "https://drive.google.com/drive/search?q={}",
    "gh": "https://github.com/search?q={}&type=repositories",
    "gl": "https://gitlab.com/search?search={}&nav_source=navbar",
    "np": "https://github.com/search?q=repo%3ANixOS%2Fnixpkgs%20{}&type=code",
    "wk": "https://en.wikipedia.org/w/index.php?fulltext=1&search={}&title=Special%3ASearch&ns0=1",
    "th": "https://www.thingiverse.com/search?q={}&page=1",
    "dh": "https://hub.docker.com/search?q={}",
}

config.set("completion.open_categories", ["searchengines", "quickmarks", "bookmarks"])

config.set("downloads.location.directory", "~/Downloads")

config.set("fileselect.handler", "external")
config.set(
    "fileselect.single_file.command", ["kitty", "-e", "ranger", "--choosefile={}"]
)
config.set(
    "fileselect.multiple_files.command", ["kitty", "-e", "ranger", "--choosefiles={}"]
)
config.set("fileselect.folder.command", ["kitty", "-e", "ranger", "--choosedir={}"])

# bindings from doom emacs
config.bind("<Alt-x>", "cmd-set-text :")
config.bind("<Space>.", "cmd-set-text :")
config.bind("<Space>b", "bookmark-list")
config.bind("<Space>h", "history")
config.bind("<Space>gh", "open https://github.com")
config.bind("<Space>gl", "open https://gitlab.com")
config.bind("<Space>gc", "open https://codeberg.org")
if secretsExists:
    config.bind("<Space>gg", "open " + qutesecrets.mygiteadomain)
config.bind("<Ctrl-p>", "completion-item-focus prev", mode="command")
config.bind("<Ctrl-n>", "completion-item-focus next", mode="command")
config.bind("<Ctrl-p>", "fake-key <Up>", mode="normal")
config.bind("<Ctrl-n>", "fake-key <Down>", mode="normal")
config.bind("<Ctrl-p>", "fake-key <Up>", mode="insert")
config.bind("<Ctrl-n>", "fake-key <Down>", mode="insert")
config.bind("<Ctrl-p>", "fake-key <Up>", mode="passthrough")
config.bind("<Ctrl-n>", "fake-key <Down>", mode="passthrough")

# bindings from vimium
config.bind("t", "open -t")
config.bind("x", "tab-close")
config.bind("yf", "hint links yank")
config.bind("<Ctrl-Tab>", "tab-next")
config.bind("<Ctrl-Shift-Tab>", "tab-prev")

# passthrough bindings
config.bind("<Shift-Escape>", "mode-leave", mode="passthrough")
config.bind("<Ctrl-T>", "open -t", mode="passthrough")
config.bind("<Ctrl-W>", "tab-close", mode="passthrough")
config.bind("<Ctrl-Tab>", "tab-next", mode="passthrough")
config.bind("<Ctrl-Shift-Tab>", "tab-prev", mode="passthrough")
config.bind("<Ctrl-B>", "cmd-set-text -s :quickmark-load -t", mode="passthrough")
config.bind("<Ctrl-O>", "cmd-set-text -s :open -t", mode="passthrough")
config.bind("<Ctrl-F>", "cmd-set-text /", mode="passthrough")
config.bind("<Ctrl-R>", "reload", mode="passthrough")
config.unbind("<Ctrl-X>")
config.unbind("<Ctrl-A>")

# spawn external programs
config.bind(",m", "hint links spawn mpv {hint-url}")
config.bind(",co", "spawn container-open")
config.bind(",cf", "hint links userscript container-open")

# TODO stylix user CSS
# current_stylesheet_directory = '~/.config/qutebrowser/themes/'
# current_stylesheet = base16_theme+'-all-sites.css'
# current_stylesheet_path = current_stylesheet_directory + current_stylesheet
# config.set('content.user_stylesheets', current_stylesheet_path)
# config.bind(',s', 'set content.user_stylesheets \'\' ')
# config.bind(',S', 'set content.user_stylesheets '+current_stylesheet_path)

# theming
c.colors.completion.fg = base05
c.colors.completion.odd.bg = base01
c.colors.completion.even.bg = base00
c.colors.completion.category.fg = base0A
c.colors.completion.category.bg = base00
c.colors.completion.category.border.top = base00
c.colors.completion.category.border.bottom = base00
c.colors.completion.item.selected.fg = base05
c.colors.completion.item.selected.bg = base02
c.colors.completion.item.selected.border.top = base02
c.colors.completion.item.selected.border.bottom = base02
c.colors.completion.item.selected.match.fg = base0B
c.colors.completion.match.fg = base0B
c.colors.completion.scrollbar.fg = base05
c.colors.completion.scrollbar.bg = base00
c.colors.contextmenu.disabled.bg = base01
c.colors.contextmenu.disabled.fg = base04
c.colors.contextmenu.menu.bg = base00
c.colors.contextmenu.menu.fg = base05
c.colors.contextmenu.selected.bg = base02
c.colors.contextmenu.selected.fg = base05
c.colors.downloads.bar.bg = base00
c.colors.downloads.start.fg = base00
c.colors.downloads.start.bg = base0D
c.colors.downloads.stop.fg = base00
c.colors.downloads.stop.bg = base0C
c.colors.downloads.error.fg = base08
c.colors.hints.fg = base00
c.colors.hints.bg = base0A
c.colors.hints.match.fg = base05
c.colors.keyhint.fg = base05
c.colors.keyhint.suffix.fg = base05
c.colors.keyhint.bg = base00
c.colors.messages.error.fg = base00
c.colors.messages.error.bg = base08
c.colors.messages.error.border = base08
c.colors.messages.warning.fg = base00
c.colors.messages.warning.bg = base0E
c.colors.messages.warning.border = base0E
c.colors.messages.info.fg = base05
c.colors.messages.info.bg = base00
c.colors.messages.info.border = base00
c.colors.prompts.fg = base05
c.colors.prompts.border = base00
c.colors.prompts.bg = base00
c.colors.prompts.selected.bg = base02
c.colors.prompts.selected.fg = base05
c.colors.statusbar.normal.fg = base0B
c.colors.statusbar.normal.bg = base00
c.colors.statusbar.insert.fg = base00
c.colors.statusbar.insert.bg = base0D
c.colors.statusbar.passthrough.fg = base00
c.colors.statusbar.passthrough.bg = base0C
c.colors.statusbar.private.fg = base00
c.colors.statusbar.private.bg = base01
c.colors.statusbar.command.fg = base05
c.colors.statusbar.command.bg = base00
c.colors.statusbar.command.private.fg = base05
c.colors.statusbar.command.private.bg = base00
c.colors.statusbar.caret.fg = base00
c.colors.statusbar.caret.bg = base0E
c.colors.statusbar.caret.selection.fg = base00
c.colors.statusbar.caret.selection.bg = base0D
c.colors.statusbar.progress.bg = base0D
c.colors.statusbar.url.fg = base05
c.colors.statusbar.url.error.fg = base08
c.colors.statusbar.url.hover.fg = base05
c.colors.statusbar.url.success.http.fg = base0C
c.colors.statusbar.url.success.https.fg = base0B
c.colors.statusbar.url.warn.fg = base0E
c.colors.tabs.bar.bg = base00
c.colors.tabs.indicator.start = base0D
c.colors.tabs.indicator.stop = base0C
c.colors.tabs.indicator.error = base08
c.colors.tabs.odd.fg = base05
c.colors.tabs.odd.bg = base00
c.colors.tabs.even.fg = base05
c.colors.tabs.even.bg = base00
c.colors.tabs.pinned.even.bg = base0B
c.colors.tabs.pinned.even.fg = base00
c.colors.tabs.pinned.odd.bg = base0B
c.colors.tabs.pinned.odd.fg = base00
c.colors.tabs.pinned.selected.even.bg = base02
c.colors.tabs.pinned.selected.even.fg = base05
c.colors.tabs.pinned.selected.odd.bg = base02
c.colors.tabs.pinned.selected.odd.fg = base05
c.colors.tabs.selected.odd.fg = base05
c.colors.tabs.selected.odd.bg = base02
c.colors.tabs.selected.even.fg = base05
c.colors.tabs.selected.even.bg = base02
