from django import template

register = template.Library()

@register.filter
def get_tech_icon(nom):
    """Retourne la classe d'icône Devicon pour une technologie"""
    icons_map = {
        # Langages
        'python': 'devicon-python-plain colored',
        'javascript': 'devicon-javascript-plain colored',
        'java': 'devicon-java-plain colored',
        'php': 'devicon-php-plain colored',
        'c': 'devicon-c-plain colored',
        'c++': 'devicon-cplusplus-plain colored',
        'ruby': 'devicon-ruby-plain colored',
        'go': 'devicon-go-plain colored',
        'rust': 'devicon-rust-plain colored',
        'typescript': 'devicon-typescript-plain colored',
        
        # Frameworks Web
        'django': 'devicon-django-plain colored',
        'flask': 'devicon-flask-original colored',
        'react': 'devicon-react-original colored',
        'vue': 'devicon-vuejs-plain colored',
        'angular': 'devicon-angularjs-plain colored',
        'laravel': 'devicon-laravel-plain colored',
        'symfony': 'devicon-symfony-original colored',
        'express': 'devicon-express-original colored',
        'nextjs': 'devicon-nextjs-plain colored',
        'nodejs': 'devicon-nodejs-plain colored',
        
        
        # Bases de données
        'mysql': 'devicon-mysql-plain colored',
        'postgresql': 'devicon-postgresql-plain colored',
        'mongodb': 'devicon-mongodb-plain colored',
        'redis': 'devicon-redis-plain colored',
        'sqlite': 'devicon-sqlite-plain colored',
        'oracle': 'devicon-oracle-original colored',
        
        # DevOps & Cloud
        'docker': 'devicon-docker-plain colored',
        'kubernetes': 'devicon-kubernetes-plain colored',
        'git': 'devicon-git-plain colored',
        'github': 'devicon-github-original colored',
        'gitlab': 'devicon-gitlab-plain colored',
        'aws': 'devicon-amazonwebservices-plain-wordmark colored',
        'azure': 'devicon-azure-plain colored',
        'jenkins': 'devicon-jenkins-plain colored',
        
        # Frontend
        'html': 'devicon-html5-plain colored',
        'css': 'devicon-css3-plain colored',
        'bootstrap': 'devicon-bootstrap-plain colored',
        'tailwind': 'devicon-tailwindcss-plain colored',
        'sass': 'devicon-sass-original colored',
        
        # Outils
        'vscode': 'devicon-vscode-plain colored',
        'linux': 'devicon-linux-plain colored',
        'ubuntu': 'devicon-ubuntu-plain colored',
        'nginx': 'devicon-nginx-original colored',
        'apache': 'devicon-apache-plain colored',
        #analyse
        'uml':'devicon-uml-plain colored',
        'merise':'devicon-merise-plain colored',
        
    }
    
    # Normaliser le nom (minuscules, sans espaces)
    nom_normalise = nom.lower().strip().replace(' ', '')
    
    # Chercher l'icône
    return icons_map.get(nom_normalise, 'bi bi-code-square')  # Icône par défaut si non trouvé

@register.filter
def has_tech_icon(nom):
    """Vérifie si une technologie a une icône"""
    icons_map = {
        'python', 'javascript', 'java', 'php', 'django', 'react', 'vue', 
        'angular', 'mysql', 'postgresql', 'mongodb', 'docker', 'git', 
        'html', 'css', 'bootstrap', 'nodejs', 'laravel', 'flask'
    }
    return nom.lower().strip().replace(' ', '') in icons_map