import React, {useState} from 'react';
import ReactDOM from 'react-dom';
import { CourseCard } from './CourseCard';
import Accordion from 'react-bootstrap/Accordion'
import { useAccordionToggle } from 'react-bootstrap/AccordionToggle';
import Header from 'components/Header';
import axios from 'axios'

function CustomToggle({ children, eventKey }) {
    const [active, setActive] = useState(false);
    
    const decoratedOnClick = useAccordionToggle(eventKey, () => {
        setActive(!active)
    });

    return (
        <div onClick={decoratedOnClick} className="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pb-2 mb-3 border-bottom">
        <h1 className="w-100 text-left h3">
            {children}
            {active ? 
                <i className="fas fa-caret-up float-right"></i> :
                <i className="fas fa-caret-down float-right"></i>
            }
        </h1>
        </div>
    );
  }

export class CourseList extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            courses: props.courses,
            courses_count: 0,
            hidden_courses_count: 0,
        };
    }

    handleHideClick = (event, url) => {
        event.preventDefault();
        
        axios.get(url)
        .then(res => res.data)
        .then(course => {
            let c_id;

            if (this.props.is_student) {
                course.is_hidden = !course.is_hidden
                c_id = course.course_offered
            } else {
                course.archive = !course.archive
                c_id = course.id
            }
            
            let courses = this.state.courses.map(c => {
                if (c.id == c_id) {
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
            
            return axios.put(url, course)
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
                request_url={c.request_url}
                onHideClick={this.handleHideClick}
            />
        ))

    renderHiddenSection = () => this.state.courses_count ? 
        (
            this.state.hidden_courses_count ? <Accordion defaultActiveKey="">
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
            <Header heading={
                !this.state.courses.length ? 'No enrolled courses' : this.state.courses_count ? 'My courses' : 'Hidden courses'
            } />
            <div className="container-fluid mt--6">
                <div className="row">
                    { !this.state.courses.length ? 
                        <CourseCard 
                            description='You are not enrolled in any course'
                            color_bg='#fff'
                            code='CODE'
                            term='404'
                            course_url=''
                            color_fg='default'
                        /> : 
                        this.renderCoursesList(false)}
                </div>
                { this.renderHiddenSection() }
            </div>
        </>)
    }
}