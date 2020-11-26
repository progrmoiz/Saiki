import React from 'react'
import ReactDOM from 'react-dom'
import { CourseCard } from './CourseCard';
import { CourseList } from './CourseList';

class CourseListApp extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
        courses: []
    };
  }

  fetchCourses = (callback) => {
      $.ajax({
          url: '/api/students/3/',
          dataType: 'json',
          cache: false,
          success: function(data) {
            callback(data)
          },
          error: function(xhr, status, err) {
            console.error(this.props.list_url, status, err.toString());
          }
      });
  }

  componentDidMount() {
    this.fetchCourses((data) => {
      this.setState({
        courses: data
      })
    })
  }

  render() {
    return (
      <CourseList list_url='/api/students/3/' courses={this.state.courses}/>
    )
  }
}

const element = <CourseListApp />;
ReactDOM.render(
  element,
  document.getElementById('course-app')
);