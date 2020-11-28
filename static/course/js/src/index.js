import React from 'react'
import ReactDOM from 'react-dom'
import { CourseCard } from './CourseCard';
import { CourseList } from './CourseList';
import axios from 'axios'

class CourseListApp extends React.Component {

  constructor(props) {
    super(props);
    axios.defaults.xsrfCookieName = 'csrftoken'
    axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
    axios.defaults.headers = {
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
        'Expires': '0',
    }
    this.state = {
        courses: []
    };
  }

  fetchCourses = (fn, error_fn) => axios.get(this.props.request_url).then(fn).catch(error_fn)
  
  componentDidMount() {
    this.fetchCourses((res) => {
      this.setState({
        courses: res.data
      })
    })
  }

  render() {
    return (
      <CourseList courses={this.state.courses} is_student={this.props.is_student} />
    )
  }
}

const element = React.createElement(CourseListApp, window.course_list_app_props);
ReactDOM.render(
  element,
  document.getElementById('course-app')
);