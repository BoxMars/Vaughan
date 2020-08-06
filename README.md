# Vaughan
#### A blog based on Django
### 2020/7/31 爷弃坑了
### 我还能抢救一下
---
# How to use?
```
    python manage.py runserver
```
---
```
D:.
│  db.sqlite3
│  index.xd
│  LICENSE
│  manage.py
│  README.md
│  SECRET_KEY
│  treefile.txt
│  
├─.idea
│  │  dataSources.local.xml
│  │  dataSources.xml
│  │  misc.xml
│  │  modules.xml
│  │  Vaughan.iml
│  │  vcs.xml
│  │  workspace.xml
│  │  
│  ├─dataSources
│  │      14dad6a0-02ea-4534-87a7-eaac4cc2af7a.xml
│  │      a7c255d4-1231-4099-95fa-2ba563c732f4.xml
│  │      
│  └─inspectionProfiles
│          profiles_settings.xml
│          
├─background
│  │  admin.py
│  │  apps.py
│  │  forms.py
│  │  models.py
│  │  tests.py
│  │  views.py
│  │  __init__.py
│  │  
│  ├─migrations
│  │  │  0001_initial.py
│  │  │  0002_auto_20200727_1756.py
│  │  │  0003_article.py
│  │  │  0004_article_created.py
│  │  │  0005_user_created.py
│  │  │  0006_auto_20200805_1955.py
│  │  │  0007_tag.py
│  │  │  0008_auto_20200805_2215.py
│  │  │  0009_article_tag.py
│  │  │  0010_auto_20200805_2217.py
│  │  │  0011_auto_20200805_2219.py
│  │  │  __init__.py
│  │  │  
│  │  └─__pycache__
│  │          0001_initial.cpython-38.pyc
│  │          0002_auto_20200727_1756.cpython-38.pyc
│  │          0003_article.cpython-38.pyc
│  │          0004_article_created.cpython-38.pyc
│  │          0005_user_created.cpython-38.pyc
│  │          0006_auto_20200805_1955.cpython-38.pyc
│  │          0007_tag.cpython-38.pyc
│  │          0008_auto_20200805_2215.cpython-38.pyc
│  │          0009_article_tag.cpython-38.pyc
│  │          0010_auto_20200805_2217.cpython-38.pyc
│  │          0011_auto_20200805_2219.cpython-38.pyc
│  │          __init__.cpython-38.pyc
│  │          
│  └─__pycache__
│          admin.cpython-38.pyc
│          forms.cpython-38.pyc
│          models.cpython-38.pyc
│          views.cpython-38.pyc
│          __init__.cpython-38.pyc
│          
├─blog
│  │  admin.py
│  │  apps.py
│  │  models.py
│  │  tests.py
│  │  views.py
│  │  __init__.py
│  │  
│  ├─migrations
│  │  │  __init__.py
│  │  │  
│  │  └─__pycache__
│  │          __init__.cpython-38.pyc
│  │          
│  └─__pycache__
│          admin.cpython-38.pyc
│          models.cpython-38.pyc
│          views.cpython-38.pyc
│          __init__.cpython-38.pyc
│          
├─static
│  └─assets
│      ├─bootstrap
│      │  ├─css
│      │  │      bootstrap.min.css
│      │  │      
│      │  └─js
│      │          bootstrap.min.js
│      │          
│      ├─css
│      │      Article-List.css
│      │      Footer-Basic.css
│      │      Footer-Dark.css
│      │      markdownit-edit-1.css
│      │      markdownit-edit.css
│      │      Navigation-Clean.css
│      │      Navigation-with-Button.css
│      │      Navigation-with-Search.css
│      │      styles.css
│      │      styles.min.css
│      │      
│      ├─fonts
│      │      fa-brands-400.eot
│      │      fa-brands-400.svg
│      │      fa-brands-400.ttf
│      │      fa-brands-400.woff
│      │      fa-brands-400.woff2
│      │      fa-regular-400.eot
│      │      fa-regular-400.svg
│      │      fa-regular-400.ttf
│      │      fa-regular-400.woff
│      │      fa-regular-400.woff2
│      │      fa-solid-900.eot
│      │      fa-solid-900.svg
│      │      fa-solid-900.ttf
│      │      fa-solid-900.woff
│      │      fa-solid-900.woff2
│      │      font-awesome.min.css
│      │      fontawesome-all.min.css
│      │      fontawesome-webfont.eot
│      │      fontawesome-webfont.svg
│      │      fontawesome-webfont.ttf
│      │      fontawesome-webfont.woff
│      │      fontawesome-webfont.woff2
│      │      FontAwesome.otf
│      │      fontawesome5-overrides.min.css
│      │      
│      ├─img
│      │  │  building.jpg
│      │  │  desk.jpg
│      │  │  loft.jpg
│      │  │  
│      │  ├─avatars
│      │  │      avatar1.jpeg
│      │  │      avatar2.jpeg
│      │  │      avatar3.jpeg
│      │  │      avatar4.jpeg
│      │  │      avatar5.jpeg
│      │  │      
│      │  └─dogs
│      │          image2.jpeg
│      │          image3.jpeg
│      │          
│      └─js
│              bs-init.js
│              chart.min.js
│              jquery.min.js
│              markdownit-edit-1.js
│              markdownit-edit-2.js
│              markdownit-edit-3.js
│              markdownit-edit.js
│              script.min.js
│              theme.js
│              
├─templates
│  ├─background
│  │  │  admin.bsdesign
│  │  │  article.html
│  │  │  index.html
│  │  │  login.html
│  │  │  profile.html
│  │  │  register.html
│  │  │  table.html
│  │  │  
│  │  └─assets
│  │      ├─bootstrap
│  │      │  ├─css
│  │      │  │      bootstrap.min.css
│  │      │  │      
│  │      │  └─js
│  │      │          bootstrap.min.js
│  │      │          
│  │      ├─css
│  │      │      markdownit-edit-1.css
│  │      │      markdownit-edit.css
│  │      │      styles.min.css
│  │      │      
│  │      ├─fonts
│  │      │      fa-brands-400.eot
│  │      │      fa-brands-400.svg
│  │      │      fa-brands-400.ttf
│  │      │      fa-brands-400.woff
│  │      │      fa-brands-400.woff2
│  │      │      fa-regular-400.eot
│  │      │      fa-regular-400.svg
│  │      │      fa-regular-400.ttf
│  │      │      fa-regular-400.woff
│  │      │      fa-regular-400.woff2
│  │      │      fa-solid-900.eot
│  │      │      fa-solid-900.svg
│  │      │      fa-solid-900.ttf
│  │      │      fa-solid-900.woff
│  │      │      fa-solid-900.woff2
│  │      │      font-awesome.min.css
│  │      │      fontawesome-all.min.css
│  │      │      fontawesome-webfont.eot
│  │      │      fontawesome-webfont.svg
│  │      │      fontawesome-webfont.ttf
│  │      │      fontawesome-webfont.woff
│  │      │      fontawesome-webfont.woff2
│  │      │      FontAwesome.otf
│  │      │      fontawesome5-overrides.min.css
│  │      │      
│  │      ├─img
│  │      │  ├─avatars
│  │      │  │      avatar1.jpeg
│  │      │  │      avatar2.jpeg
│  │      │  │      avatar3.jpeg
│  │      │  │      avatar4.jpeg
│  │      │  │      avatar5.jpeg
│  │      │  │      
│  │      │  └─dogs
│  │      │          image2.jpeg
│  │      │          image3.jpeg
│  │      │          
│  │      └─js
│  │              bs-init.js
│  │              chart.min.js
│  │              jquery.min.js
│  │              markdownit-edit-1.js
│  │              markdownit-edit-2.js
│  │              markdownit-edit-3.js
│  │              markdownit-edit.js
│  │              script.min.js
│  │              theme.js
│  │              
│  └─blog
│      │  base.html
│      │  detail.bsdesign
│      │  detail.html
│      │  index.bsdesign
│      │  index.html
│      │  
│      └─assets
│          ├─bootstrap
│          │  ├─css
│          │  │      bootstrap.min.css
│          │  │      
│          │  └─js
│          │          bootstrap.min.js
│          │          
│          ├─css
│          │      Article-Clean.css
│          │      Article-List.css
│          │      Footer-Basic.css
│          │      Footer-Dark.css
│          │      Navigation-Clean.css
│          │      Navigation-with-Button.css
│          │      Navigation-with-Search.css
│          │      styles.css
│          │      styles.min.css
│          │      
│          ├─img
│          │      beach.jpg
│          │      building.jpg
│          │      desk.jpg
│          │      loft.jpg
│          │      
│          └─js
│                  jquery.min.js
│                  
├─Vaughan
│  │  asgi.py
│  │  settings.py
│  │  urls.py
│  │  wsgi.py
│  │  __init__.py
│  │  
│  └─__pycache__
│          settings.cpython-38.pyc
│          urls.cpython-38.pyc
│          wsgi.cpython-38.pyc
│          __init__.cpython-38.pyc
│          
└─__pycache__
        manage.cpython-38.pyc
        
```