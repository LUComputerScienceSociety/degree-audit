Accounts.onLogin(function(){
     FlowRouter.go('/AdminDashboard');
});

FlowRouter.triggers.enter([function(context,redirect){
    if(!Meteor.userId()){
        FlowRouter.go('/')
    }
}]);

FlowRouter.route('/', {
    name: 'welcome',
    action(){
        if(Meteor.userId()){
            FlowRouter.go('/main')
        }
        BlazeLayout.render('Welcome');
    }
});

FlowRouter.route('/AdminDashboard', {
    name: 'AdminDashboard',
    action(){
        BlazeLayout.render('Main', {main: 'AdminDashboard'});
    }
});
