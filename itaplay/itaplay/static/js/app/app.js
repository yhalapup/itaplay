'use strict';

var itaplay = angular.module('itaplay', ['ngRoute', 'ngMaterial', 'ngFileUpload', 'ngMessages']);


itaplay.config(function($routeProvider) {
    $routeProvider
    	.when('/test', {
            templateUrl: '../../../static/js/app/test/views/test.html',
            controller: TestController
        })
        .when('/allclips', {
            templateUrl: '../../../static/js/app/clips/views/allclips.html',
            controller: 'AllClipController'
        })
        .when('/test1', {
            templateUrl: '../../../static/js/app/test/views/test1.html',
            
        })
        
        .when('/clip/pk=:pk/', {
            templateUrl: '../../../static/js/app/clips/views/current_clip.html',
            controller: 'CurrentClipController'
        })
        .when('/clips', {
            templateUrl: '../../../static/js/app/clips/views/add_clip.html',
            controller: 'ClipController'
                                
        })
        .otherwise({redirectTo: '/test'});
})
.run(function($log) {
    $log.info("Starting up");
})

// choose colors for our theme
.config(function($mdThemingProvider) {
    $mdThemingProvider.theme('default')
      .primaryPalette('teal')
      .accentPalette('blue');
});

itaplay.config(['$httpProvider', function($httpProvider) {
$httpProvider.defaults.xsrfCookieName = 'csrftoken';
$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);



