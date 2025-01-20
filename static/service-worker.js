const CACHE_NAME = "quiz-app-cache-v2";
const urlsToCache = [
    "/",
    "/static/quiz.html", // Ana quiz HTML dosyası
    "/static/style.css", // Eğer bir CSS dosyanız varsa
    "/static/questions.json", // Soruların olduğu JSON dosyası
    "/static/icon.png" // Bir ikon eklemek isterseniz
];

// Kurulum sırasında gerekli dosyaları önbelleğe al
self.addEventListener("install", function(event) {
    event.waitUntil(
        caches.open(CACHE_NAME).then(function(cache) {
            return cache.addAll(urlsToCache);
        })
    );
});

// Gelen ağ isteklerini yakala ve önbellekten yanıtla
self.addEventListener("fetch", function(event) {
    event.respondWith(
        caches.match(event.request).then(function(response) {
            return response || fetch(event.request);
        })
    );
});

// Eski önbellekleri temizle
self.addEventListener("activate", function(event) {
    event.waitUntil(
        caches.keys().then(function(cacheNames) {
            return Promise.all(
                cacheNames.map(function(cacheName) {
                    if (cacheName !== CACHE_NAME) {
                        return caches.delete(cacheName);
                    }
                })
            );
        })
    );
});
