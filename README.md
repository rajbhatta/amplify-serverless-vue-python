# 1. How project is created ? #
## 1.1 Install NPM ##
```js

```

## 1.2 Install VUE CLI ##
```js
sudo npm install -g @vue/cli
```

## 1.3 Create Vue Project using CLI ##
```js
 vue create clientmgmt
```

# 2. Add Vuex #
## 2.1 Add vuex ##
```js
vue add vuex
```

# 3. Install Tailwind CSS #
```js
vue add tailwind 
```

# 4. Install AWS Amplify dependency for UI #
```js
npm install aws-amplify @aws-amplify/ui-components
```
- Reference: https://docs.amplify.aws/start/getting-started/setup/q/integration/vue/#initialize-a-new-backend
- Make sure to run command:
```js 
amplify push -y
```
to make amplify available for UI
