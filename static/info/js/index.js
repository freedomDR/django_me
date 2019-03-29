
var myMusic = new Vue({
                      el:'#my_music',
                      data:{
                          name: 'vue.js'
                      },
                      methods:{
                          myalert: function(event){
                              console.log('hello'+this.name+'!')
                              alert('hello '+this.name+'!')
                          }
                      }

})
myMusic.myalert()
