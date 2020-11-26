import React from 'react';
import ReactDOM from 'react-dom';
import $ from 'jquery';
import { CourseCard } from './CourseCard';
import Accordion from 'react-bootstrap/Accordion'
import { useAccordionToggle } from 'react-bootstrap/AccordionToggle';
import * as lib from './lib.js';
import { Header } from './Header';

function CustomToggle({ children, eventKey }) {
    const decoratedOnClick = useAccordionToggle(eventKey, () => {});
    return (
        <div onClick={decoratedOnClick} className="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pb-2 mb-3 border-bottom">
        <h1 className="w-100 text-left h3">
            {children}<i className="ni ni-bold-down float-right"></i>
        </h1>
        </div>
    );
  }

export class CourseList extends React.Component {
    constructor(props) {
        super(props);
        lib.jquery_ajax_setup('csrftoken');
        console.log('props.courses', props.courses)
        this.state = {
            courses: props.courses,
            courses_count: 0,
            hidden_courses_count: 0,
        };
        this.handleHideClick = this.handleHideClick.bind(this);
    }

    handleHideClick(event, url) {
        event.preventDefault();
        console.log('click', url)
        
        $.ajax({
          method: 'GET',
          url: url,
        //   data: data,
          dataType: 'json',
          cache: false,
          success: function(data, textStatus, xhr) {
            console.log('search and found data', data)
            console.log(this.state)
            data.is_hidden = !data.is_hidden
            
            let courses = this.state.courses.map(c => {
                console.log(c.id == data.course_offered, c.id, data.course_offered)
                if (c.id == data.course_offered) {
                    return {
                        ...c,
                        is_hidden: !c.is_hidden
                    }
                }
                return c;
            });

            this.setState({
                courses: courses,
                courses_count: this.getCoursesCount(courses),
                hidden_courses_count: this.getHiddenCoursesCount(courses)
            });

            $.ajax({
                method: 'PUT',
                url: url,
                data: data,
                dataType: 'json',
                cache: false,
                success: function(data, textStatus, xhr) {
                    console.log('success')
                }.bind(this),
                error: this.handle_ajax_error
              })
          }.bind(this),
          error: this.handle_ajax_error
        })
    }

    getHiddenCoursesCount = (courses) => courses.filter(a => a.is_hidden).length

    getCoursesCount = (courses) => courses.filter(a => !a.is_hidden).length

    componentWillReceiveProps(nextProps) {
        // You don't have to do this check first, but it can help prevent an unneeded render
        if (nextProps.courses !== this.state.courses) {
          this.setState({ 
              courses: nextProps.courses,
              courses_count: this.getCoursesCount(nextProps.courses),
              hidden_courses_count: this.getHiddenCoursesCount(nextProps.courses)
          });
        }
      }

    renderCoursesList = (hidden) => this.state.courses.filter((c, i) => c.is_hidden == hidden).map((c, i) => (
            <CourseCard 
                description={c.description}
                code={c.code}
                is_hidden={c.is_hidden}
                term={c.term}
                slug={c.slug}
                course_url={c.href}
                color_bg={c.color_bg}
                color_fg={c.color_fg}
                key={i}
                course_enrollment_url={c['course-enrollment-url']}
                onHideClick={this.handleHideClick}
            />
        ))

    renderHiddenSection = () => this.state.courses_count ? 
        (
            this.state.hidden_courses_count ? <Accordion defaultActiveKey="0">
            <CustomToggle eventKey="0">Hidden Courses</CustomToggle>
            <Accordion.Collapse eventKey="0">
                <div className="row">
                    { this.renderCoursesList(true) }
                </div>
            </Accordion.Collapse>
            </Accordion> : ''
         ) : 
        <div className="row">
            { this.renderCoursesList(true) }
        </div>

    render() {
        return (<>
            <Header heading={this.state.courses_count ? 'My courses' : 'Hidden courses'} />
            <div className="container-fluid mt--6">
                <div className="row">
                    { this.renderCoursesList(false) }
                </div>
                { this.renderHiddenSection() }
            </div>
        </>)
    }
}