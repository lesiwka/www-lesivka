const CACHE = 'cache-v7';
const timeout = 400;

self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE).then((cache) => cache.addAll([
            '/',
            '/abetka',
            '/prikladi',
            '/zastosunki',
            '/konverter',
            '/lat',
            '/lat/abetka',
            '/lat/prikladi',
            '/lat/zastosunki',
            '/lat/konverter',
            '/css/bootstrap.min.css',
            '/css/style.css',
            '/fonts/NotoSans-Regular.woff2',
            '/images/facebook.png',
            '/js/bootstrap.min.js',
            '/js/index.js',
            '/js/jquery.slim.min.js',
            '/js/lesiwka.js',
            '/js/popper.min.js',
            '/icons/download.png',
            '/images/kbd-en-lesiwka.png',
            '/images/kbd-en-lesiwka-alt.png',
            '/images/kbd-uk-lesiwka.png',
            '/images/kbd-uk-lesiwka-phonetic.png',
            '/images/chrome.png',
            '/images/play-market.png',
            '/images/telegram.png',
            '/site.webmanifest',
            '/android-chrome-192x192.png',
            '/android-chrome-512x512.png',
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
