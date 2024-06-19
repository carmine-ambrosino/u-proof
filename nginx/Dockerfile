# -------------------------------------------------------
# Nginx Docker File
# -------------------------------------------------------
FROM nginx:alpine

# Create directory for ssl certificates
RUN mkdir -p /etc/ssl/nginx
    
# Install openssl
RUN apk --update --no-cache add openssl
    
# Generate self-signed certificates
RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/nginx/cert.key -out /etc/ssl/nginx/cert.crt -subj "/C=IT/ST=Italy/L=City/O=UProofApp/CN=uproof"
    
# Copy NGINX configuration file
COPY nginx.conf /etc/nginx/nginx.conf
    
# Expose port 80 to the outside world
EXPOSE 80 443
    
# Command to start NGINX and keep it running in the foreground
CMD ["nginx", "-g", "daemon off;"]