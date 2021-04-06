FROM node:10.24

WORKDIR /frontend

COPY package.json /frontend/package.json
RUN npm install
COPY . /frontend
EXPOSE 4200
CMD ["npm", "start"]
