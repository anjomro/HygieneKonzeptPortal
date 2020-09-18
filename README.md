# HygieneKonzeptPortal (Hygiene Plan Portal)
This project is meant to provide an easy way of announcing multiple hygiene plans publicly. New Plans can be added via the Django admin interface (/admin).

## Deployment
The recommended and easiest way of deploying the OpenSoundStream Server is to use the available docker container.

    docker run -d -p 8109:8000 \
        --mount source=hygiene-db,target=/portal/db \
         --name hygieneportal \
         anjomro/hygieneportal

##### Parameter Explanation:
- `-d` Run the server in detached mode (-> in Background)
- `-p 8099:8000` Expose port 8000 (HTTP Interface) of container to local port 8109 the local port can be changed to any free port.
- `--mount source=hygiene-db,target=/portal/db \` A docker volume is used to persist the sqlite-database: If the container is deleted and instanciated again the Volume and therefore teh Database is used again.
- `--name hygieneportal` Name the container 'hygieneportal' for future reference
- `anjomro/hygieneportal` Specifies to use the anjomro/hygieneportal image.

#### Additional Parameters (that might be useful)
- `-e DJANGO_HOST=my-domain.tld` Add my-domain.tld to the allowed host if exposing the Port directly (not recommend!).  The recommended way is to use a reverse proxy The allowed ports include `localhost` and `127.0.0.1` by default.

#### Reverse Proxy Config for Apache

    <VirtualHost *:443> #Using TLS-Encryption is strongly recommended 
	    ServerName my-domain.tld  
	    ProxyPass / http://localhost:8109/  
	    ProxyPassReverse / http://localhost:8109/
	    
	    #For Let's Encrypt confifguration
	    Include /etc/letsencrypt/options-ssl-apache.conf SSLCertificateFile
	    /etc/letsencrypt/live/my-domain.tld-0001/fullchain.pem SSLCertificateKeyFile
	    /etc/letsencrypt/live/my-domain.tld-0001/privkey.pem
	</VirtualHost>
  
  #### Reverse Proxy for Caddyfile
  
    my-domain.tld {
      reverse_proxy localhost:8109
    }
  
