var gulp = require('gulp');
var jsmin = require('gulp-jsmin');
var rename = require('gulp-rename');

gulp.task('js', function () {
    gulp.src([
        './scrumboard/statics/scrumboard/js/*.js',
        './scrumboard/statics/scrumboard/js/**/*.js',
    ])
        .pipe(jsmin())
        .pipe(rename({suffix: '.min'}))
        .pipe(gulp.dest('./statics/dist'));
});

gulp.task('default', ['js'])