'use strict';

var itaplay = angular.module('itaplay', ['ngRoute','ngMaterial']);


itaplay.config(function($routeProvider) {
    $routeProvider
        .when('/test/', {
            templateUrl: '../../../static/js/app/test/views/test.html',
            controller: TestController
        })
        .otherwise({redirectTo: '/test'})

        .when('/company/', {
            templateUrl: '../../../static/js/app/company/views/all_companies.html',
            controller: AllCompanyController
            
           
        })
       .otherwise({redirectTo: '/test'})
       
       .when('/company/add_new/', {
            templateUrl: '../../../static/js/app/company/views/add_company.html',
            controller: CompanyAddController
                        
           
        })
        .otherwise({redirectTo: '/company/'});
})

.run(function($log) {
    $log.info("Starting up");
})
// choose colors for our theme
.config(function($mdThemingProvider) {
    $mdThemingProvider.theme('default')
      .primaryPalette('teal')
      .accentPalette('blue')
      .dark();


})

.config(function($httpProvider){
$httpProvider.defaults.xsrfCookieName = 'csrftoken';
$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});