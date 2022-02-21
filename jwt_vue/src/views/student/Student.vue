<template>
<div>
  <h2>学生列表</h2>
    <ul v-for="(student,index) in students" :key="index">
      <li>{{student.name}}</li>
      <li>{{student.sex}}</li>
      <li>{{student.sid}}</li>
    </ul>
</div>
</template>

<script>
import { getStudent } from '@/api/student'

export default {
  name: 'Student',
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
