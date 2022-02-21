<template>
  <div>
    <h1>登录成功!</h1>
    <div class="router" v-for="(router,index) in addRoutes" :key="index">
      <router-link :to="router.path">API接口: {{router.name}},用户权限是: {{router.meta}}</router-link>
      <div class="home" v-if="router.name=== 'home'">
        <h1>用户信息是:</h1>
        <li>用户ID: {{id}}</li>
        <li>用户名称: {{username}}</li>
        <li>用户权限: {{levels}}</li>
      </div>
      <div class="student" v-if="router.name === 'student'">
        <h2>学生列表</h2>
        <ul v-for="(student,index) in students" :key="index">
          <li>{{student.name}}</li>
          <li>{{student.sex}}</li>
          <li>{{student.sid}}</li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapState } from 'vuex'
import { getStudent } from '@/api/student'
export default {
  name: 'index',
  computed: {
    ...mapState(['routes', 'addRoutes']),
    ...mapGetters(['token', 'id', 'username', 'levels'])
  },
  data () {
    return {
      students: []
    }
  },
  created () {
    getStudent(this.token).then(response => {
      this.students = response
      console.log(this.students)
    })
  }
}
</script>

<style scoped>

</style>
