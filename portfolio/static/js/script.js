(function () {
        'use strict';
        
        const toggle = document.getElementById('theme-toggle');
        const icon = document.getElementById('theme-icon');
        const text = document.getElementById('theme-text');

        function applyTheme(theme) {
            document.documentElement.setAttribute('data-theme', theme);
            localStorage.setItem('theme', theme);
            
            if (theme === 'dark') {
                icon.className = 'bi bi-sun-fill';
                text.textContent = 'Mode clair';
                toggle.setAttribute('aria-label', 'Passer en mode clair');
            } else {
                icon.className = 'bi bi-moon-fill';
                text.textContent = 'Mode sombre';
                toggle.setAttribute('aria-label', 'Passer en mode sombre');
            }
        }

        // Initialiser l'icône selon le thème actuel
        const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
        applyTheme(currentTheme);

        // Basculer entre les thèmes au clic
        if (toggle) {
            toggle.addEventListener('click', function () {
                const newTheme = document.documentElement.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
                applyTheme(newTheme);
            });
        }

        // Écouter les changements de préférence système
        if (window.matchMedia) {
            const darkModeQuery = window.matchMedia('(prefers-color-scheme: dark)');
            darkModeQuery.addEventListener('change', function(e) {
                if (!localStorage.getItem('theme')) {
                    applyTheme(e.matches ? 'dark' : 'light');
                }
            });
        }
    })();