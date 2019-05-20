const CACHE = 'cache-v3';
const timeout = 400;

self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE).then((cache) => cache.addAll([
            '/',
            '/abetka',
            '/prikladi',
            '/zastosinki',
            '/konverter',
            '/lat',
            '/lat/abetka',
            '/lat/prikladi',
            '/lat/zastosinki',
            '/lat/konverter',
            '/css/style.css',
            '/fonts/NotoSans-Regular.woff2',
            '/images/facebook.png',
            '/js/lesivka.js',
            '/js/index.js',
            '/images/kbd-ua-lesivka.png',
            '/images/kbd-ua-lesivka-eng.png',
            '/images/kbd-ua-lesivka-eng-alt.png',
            '/images/chromium.png',
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
        cache.match(request).then((matching) =>
            matching || new Response(new Blob(), {status: 404})
        )
    );
}

function updateCache(request, response) {
    return caches.open(CACHE).then((cache) =>
        cache.put(request, response.clone()).then(() => response)
    );
}
