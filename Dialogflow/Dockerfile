FROM launcher.gcr.io/google/nodejs

# Copy application code.
COPY app.js app.js
COPY app_js.yaml app_js.yaml
COPY package.json package.json
COPY XXXX-firebase-adminsdk-l5rib-XXXX.json XXXX-firebase-adminsdk-l5rib-XXXX.json


# Install dependencies.
RUN npm --unsafe-perm install &&\
    npm install -g firebase-tools
CMD [ "node", "app.js" ]
