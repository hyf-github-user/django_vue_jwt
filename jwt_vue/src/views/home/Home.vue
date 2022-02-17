<template>
  <div class="home">
    <h1>首页，跳转成功</h1>
    <h1>用户信息是:</h1>
    <li>用户ID: {{id}}</li>
    <li>用户名称: {{username}}</li>
    <li>用户权限: {{levels}}</li>
    <hr>
    <h2>学生列表</h2>
    <ul v-for="(student,index) in students" :key="index">
      <li>{{student.name}}</li>
      <li>{{student.sex}}</li>
      <li>{{student.sid}}</li>
    </ul>
  </div>
</template>

<script>
// @ is an alias to /src
import { mapGetters } from 'vuex'
import { getStudent } from '@/api/student'
export default {
  name: 'Home',
  data () {
    return {
      students: []
    }
  },
  computed: {
    ...mapGetters(['token', 'id', 'username', 'levels'])
  },
  created () {
    getStudent(this.token).then(response => {
      this.students = response
      console.log(this.students)
    })
  }
}
</script>
