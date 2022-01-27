<template>
  <div id="login-container">
    <div style="text-align: center;height: 50px">
      登录
    </div>
    <el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
      <el-form-item label="账号" prop="username">
        <el-input type="text" v-model="ruleForm.username" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="密码" prop="password">
        <el-input type="password" v-model="ruleForm.password" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm('ruleForm')">提交</el-button>
        <el-button @click="resetForm('ruleForm')">重置</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import { mapMutations } from 'vuex'
import { login } from '@/api/user'

export default {
  name: 'login',
  data () {
    const validateUser = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入用户名'))
      } else {
        callback()
      }
    }
    const validatePass = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入密码'))
      } else {
        callback()
      }
    }
    return {
      ruleForm: {
        username: '',
        password: ''
      },
      // 自定义规则
      rules: {
        username: [
          {
            validator: validateUser,
            trigger: 'blur'
          }
        ],
        password: [
          {
            validator: validatePass,
            trigger: 'blur'
          }
        ]
      },
      isLogin: false
    }
  },
  methods: {
    ...mapMutations(['mSetTokenInfo']),
    // 提交登录表单
    submitForm (formName) {
      this.$refs[formName].validate((valid) => { // 校验表单数据
        if (valid) {
          console.log(this.ruleForm.username)
          login(this.ruleForm).then(response => {
            console.log('response:', response)
            // 保存token
            this.$store.commit('mSetTokenInfo', response.access)
            this.$router.push('/home')
          }).catch(error => {
            console.log(error)
          })
        } else {
          console.log('校验失败!')
          return false
        }
      })
    },
    // 重置表单
    resetForm (formName) {
      this.$refs[formName].resetFields()
    }
  }
}
</script>

<style scoped>
body {
  margin: 0;
}

#login-container {
  width: 400px;
  height: 290px;
  background: #e5e9f2;
  position: absolute;
  left: 50%;
  top: 50%;
  margin-left: -220px;
  margin-top: -170px;
  border-radius: 5px;
  padding-top: 40px;
  padding-right: 40px;
}
</style>
