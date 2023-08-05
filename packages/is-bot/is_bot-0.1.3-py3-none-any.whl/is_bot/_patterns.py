default_patterns = {
    " daum[ /]",
    " deusu/",
    "(?:^| )site",
    "@[a-z]",
    "\\(at\\)[a-z]",
    "\\(github\\.com/",
    "\\[at\\][a-z]",
    "^12345",
    "^<",
    "^[\\w \\.]+/v?\\d+(\\.\\d+)?(\\.\\d{1,10})?$",
    "^[\\w]+$",
    "^[^ ]{50,}$",
    "^ace explorer",
    "^acoon",
    "^active",
    "^ad muncher",
    "^anglesharp/",
    "^anonymous",
    "^apple-pubsub/",
    "^astute srm",
    "^avsdevicesdk/",
    "^axios/",
    "^bidtellect/",
    "^biglotron",
    "^blackboard safeassign",
    "^blocknote.net",
    "^braze sender",
    "^captivenetworksupport",
    "^castro",
    "^cf-uc ",
    "^clamav[ /]",
    "^cobweb/",
    "^coccoc",
    "^custom",
    "^dap ",
    "^ddg[_-]android",
    "^discourse",
    "^dispatch/\\d",
    "^downcast/",
    "^duckduckgo",
    "^email",
    "^enigma browser",
    "^evernote clip resolver",
    "^facebook",
    "^faraday",
    "^fdm[ /]\\d",
    "^getright/",
    "^gozilla/",
    "^hatena",
    "^hobbit",
    "^hotzonu",
    "^hwcdn/",
    "^infox-wisg",
    "^invision",
    "^jeode/",
    "^jetbrains",
    "^jetty/",
    "^jigsaw",
    "^linkdex",
    "^lwp[-: ]",
    "^mailchimp\\.com$",
    "^metauri",
    "^microsoft bits",
    "^microsoft data",
    "^microsoft office existence",
    "^microsoft office protocol discovery",
    "^microsoft windows network diagnostics",
    "^microsoft-cryptoapi",
    "^microsoft-webdav-miniredir",
    "^movabletype",
    "^mozilla/\\d\\.\\d \\(compatible;?\\)$",
    "^mozilla/\\d\\.\\d \\w*$",
    "^my browser$",
    "^navermailapp",
    "^netsurf",
    "^node-superagent",
    "^octopus",
    "^offline explorer",
    "^pagething",
    "^panscient",
    "^perimeterx",
    "^php",
    "^postman",
    "^postrank",
    "^python",
    "^read",
    "^reed",
    "^request-promise$",
    "^restsharp/",
    "^shareaza",
    "^shockwave flash",
    "^snapchat",
    "^space bison",
    "^sprinklr",
    "^svn",
    "^swcd ",
    "^t-online browser",
    "^taringa",
    "^test certificate info",
    "^the knowledge ai",
    "^thinklab",
    "^thumbor/",
    "^traackr.com",
    "^tumblr/",
    "^vbulletin",
    "^venus/fedoraplanet",
    "^w3c",
    "^webbandit/",
    "^webcopier",
    "^wget",
    "^whatsapp",
    "^www-mechanize",
    "^xenu link sleuth",
    "^yahoo",
    "^yandex",
    "^zdm/\\d",
    "^zeushdthree",
    "^zoom marketplace/",
    "adbeat\\.com",
    "appinsights",
    "archive",
    "ask jeeves/teoma",
    "bit\\.ly/",
    "bluecoat drtr",
    "bot",
    "browsex",
    "burpcollaborator",
    "capture",
    "catch",
    "check",
    "chrome-lighthouse",
    "chromeframe",
    "client",
    "cloud",
    "crawl",
    "daemon",
    "dareboost",
    "datanyze",
    "dataprovider",
    "dejaclick",
    "dmbrowser",
    "download",
    "evc-batch/",
    "feed",
    "fetch",
    "firephp",
    "freesafeip",
    "ghost",
    "gomezagent",
    "google",
    "headlesschrome/",
    "http",
    "httrack",
    "hubspot marketing grader",
    "hydra",
    "ibisbrowser",
    "images",
    "index",
    "ips-agent",
    "java",
    "library",
    "mail\\.ru/",
    "manager",
    "monitor",
    "morningscore/",
    "neustar wpm",
    "news",
    "nutch",
    "offbyone",
    "optimize",
    "pagespeed",
    "parse",
    "perl",
    "phantom",
    "pingdom",
    "powermarks",
    "preview",
    "probe",
    "proxy",
    "ptst[ /]\\d",
    "reader",
    "rexx;",
    "rigor",
    "rss",
    "scan",
    "scrape",
    "search",
    "serp ?reputation ?management",
    "server",
    "sogou",
    "sparkler/",
    "spider",
    "statuscake",
    "stumbleupon\\.com",
    "supercleaner",
    "synapse",
    "synthetic",
    "taginspector/",
    "toolbar",
    "torrent",
    "tracemyfile",
    "transcoder",
    "trendsmapresolver",
    "twingly recon",
    "url",
    "valid",
    "virtuoso",
    "wappalyzer",
    "webglance",
    "webkit2png",
    "websitemetadataretriever",
    "whatcms/",
    "wordpress",
    "zgrab",
}

# Cubot device
default_patterns.remove('bot')
default_patterns.add('(?<! cu)bot')

# Android webview(?)
default_patterns.remove('google')
default_patterns.add('(?<! (channel/|google/))google(?!(app|/google| pixel))')

# Yandex browser
default_patterns.remove('search')
default_patterns.add('(?<! (ya|yandex))search')

# libhttp browser
default_patterns.remove('http')
default_patterns.add('(?<!(lib))http')

# java based browser
default_patterns.remove('java')
default_patterns.add('java(?!;)')

# Mozilla nightly build https://github.com/mozilla-mobile/android-components/search?q=MozacFetch
default_patterns.remove('fetch')
default_patterns.add('(?<!(mozac))fetch')
