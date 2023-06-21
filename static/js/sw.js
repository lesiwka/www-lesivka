const CACHE = 'cache-v9';
const timeout = 400;

self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE).then((cache) => cache.addAll([
            '/',
            '/abetka',
            '/pryklady',
            '/zastosunky',
            '/konverter',
            '/lat',
            '/lat/abetka',
            '/lat/pryklady',
            '/lat/zastosunky',
            '/lat/konverter',
            '/static/css/bootstrap.min.css',
            '/static/css/style.css',
            '/static/fonts/NotoSans-Regular.woff2',
            '/static/images/facebook.png',
            '/static/js/bootstrap.min.js',
            '/static/js/index.js',
            '/static/js/jquery.slim.min.js',
            '/static/js/lesiwka.js',
            '/static/js/popper.min.js',
            '/static/icons/download.png',
            '/static/images/kbd-en-lesiwka.png',
            '/static/images/kbd-en-lesiwka-alt.png',
            '/static/images/kbd-uk-lesiwka.png',
            '/static/images/kbd-uk-lesiwka-phonetic.png',
            '/static/images/chrome.png',
            '/static/images/play-market.png',
            '/static/images/telegram.png',
            '/static/site.webmanifest',
            '/static/icons/android-chrome-192x192.png',
            '/static/icons/android-chrome-512x512.png',
        ]))
    );
});

self.addEventListener('fetch', (event) => {
    event.respondWith(fromNetwork(event.request, timeout)
        .then((response) => updateCache(event.request, response))
        .catch(() => fromCache(event.request))
    );
});

function fromNetwork(request, timeout) {
    return new Promise((fulfill, reject) => {
        const timeoutId = setTimeout(reject, timeout);
        fetch(request).then((response) => {
            clearTimeout(timeoutId);
            fulfill(response);
        }, reject);
    });
}

function fromCache(request) {
    return caches.open(CACHE).then((cache) =>
        cache.match(request, {ignoreSearch: true}).then((matching) =>
            matching || new Response(new Blob(), {status: 404})
        )
    );
}

function updateCache(request, response) {
    return caches.open(CACHE).then((cache) =>
        cache.put(request, response.clone()).then(() => response)
    );
}
