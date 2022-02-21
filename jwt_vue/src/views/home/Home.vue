<template>
  <div class="home">
    <h1>首页，跳转成功</h1>
    <h1>用户信息是:</h1>
    <li>用户ID: {{id}}</li>
    <li>用户名称: {{username}}</li>
    <li>用户权限: {{levels}}</li>
  </div>
</template>

<script>
// @ is an alias to /src
import { mapGetters } from 'vuex'

export default {
  name: 'Home',
  computed: {
    ...mapGetters(['token', 'id', 'username', 'levels'])
  }
}
</script>
