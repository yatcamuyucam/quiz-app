const CACHE_NAME = "quiz-app-cache-v2";
const urlsToCache = [
    "/",
    "/quiz.html", // Ana HTML dosyası
    "/static/style.css", // CSS dosyanız
    "/static/questions.json", // JSON dosyası
    "/static/icon.png" // İkon dosyanız (isteğe bağlı)
];

// Kurulum sırasında gerekli dosyaları önbelleğe al
self.addEventListener("install", function (event) {
    event.waitUntil(
        caches.open(CACHE_NAME).then(function (cache) {
            return cache.addAll(urlsToCache);
        })
    );
});

// Gelen ağ isteklerini yakala ve önbellekten yanıtla
self.addEventListener("fetch", function (event) {
    event.respondWith(
        caches.match(event.request).then(function (response) {
            // Önce önbelleği kontrol et, yoksa ağdan çek
            return response || fetch(event.request);
        })
    );
});

// Eski önbellekleri temizle
self.addEventListener("activate", function (event) {
    event.waitUntil(
        caches.keys().then(function (cacheNames) {
            return Promise.all(
                cacheNames.map(function (cacheName) {
                    if (cacheName !== CACHE_NAME) {
                        return caches.delete(cacheName);
                    }
                })
            );
        })
    );
});
