# portfolio/views.py
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.http import require_http_methods
import json

# Project data dictionary
PROJECTS_DATA = {
    'project-management': {
        'id': 'project-management',
        'title': 'Project Management System',
        'subtitle': 'Comprehensive Task & Project Tracking Solution',
        'description': 'Comprehensive project management solution with task management, role-based permissions, and fully documented APIs for seamless frontend integration.',
        'technologies': ['Django REST', 'JWT', 'PostgreSQL', 'Permissions'],
        'icon': 'fas fa-tasks',
        'period': 'Sep 2024 - Dec 2024',
        'status': 'Completed',
        'role': 'Backend Developer',
        'team_size': '5 members',
        'full_description': '''
            A full-featured project management system built to help teams collaborate effectively. 
            The system provides task tracking, project timelines, team management, and detailed 
            reporting capabilities with a focus on API-first design.
        ''',
        'key_features': [
            'Structured project and task management with parent-child hierarchy, milestones, and stage-based workflow structures',
            'Automated email and in-app notifications for task creation, task completion, and user assignment to projects',
            'Role-based access control (Admin, Manager, Team Member)',
            'Time tracking and productivity analytics',
            'File attachments and document management',
            'Commenting and collaboration features',
            'Interactive dashboard with flag-wise task distribution (Normal, High, Urgent)',
            'Visual task analytics showing total, completed, pending, and overdue tasks using charts',
        ],
        'technical_highlights': [
            {
                'title': 'API Design',
                'description': 'Designed RESTful APIs following best practices with versioning, pagination, and filtering.',
            }, 
            {
                'title': 'Permission System',
                'description': 'Implemented custom permission framework allowing fine-grained control over resource access.',
            },
            {
                'title': 'Real-time Updates',
                'description': 'Integrated Django Channels for WebSocket-based real-time notifications.',
            },
            {
                'title': 'Performance',
                'description': 'Optimized API response times to under 200ms using caching and query optimization.',
            },
        ],
        'challenges_solutions': [
            {
                'challenge': 'Complex nested relationships between projects, tasks, and subtasks',
                'solution': 'Designed efficient database schema with proper foreign keys and implemented recursive serializers',
            },
            {
                'challenge': 'Frontend-backend API integration complexities',
                'solution': 'Created detailed API documentation with examples and provided comprehensive testing support',
            },
        ],
        'outcomes': [
            'Improved team collaboration efficiency by 30%',
            'Reduced project delivery time through better tracking',
            'Successfully integrated with Vue.js frontend application',
            'Achieved 99.9% API uptime in production',
        ],
    },
    'billcostro': {
        'id': 'billcostro',
        'title': 'Billcostro',
        'subtitle': 'Enterprise Cost Management System',
        'description': 'Enterprise cost management system with modular architecture, featuring 60+ models across 5+ apps with role-based workflows and asset tracking.',
        'technologies': ['Django REST', 'PostgreSQL', 'JWT', 'Razor Pay'],
        'icon': 'fas fa-chart-line',
        'period': 'Jan 2025 - May 2025',
        'status': 'Completed',
        'role': 'Backend Developer',
        'team_size': '4 members',
        'full_description': '''
            Billcostro is a comprehensive enterprise-level cost management system designed to streamline 
            financial operations for large organizations. The system features a modular architecture with 
            over 60 database models distributed across 5+ specialized Django apps.
        ''',
        'key_features': [
            'Role-based workflow management with multiple user hierarchies',
            'Integrated push notification alerts for critical user actions handled by selected API endpoints.',
            'Automated billing and invoice generation',
            'Integration with Razor Pay payment gateway',
            'Implemented role-based reporting and analytics dashboards, supported by separate APIs for each user role.',
            'Developed Python scripts for initializing and maintaining master datasets including country, currency, location, employee, and asset information.',
            'Built 50+ email-sending functions with Celery for background task execution.',
            'JWT-based authentication and authorization',
        ],
        'technical_highlights': [
            {
                'title': 'Modular Architecture',
                'description': 'Designed and implemented 5+ Django apps with 60+ models, ensuring scalability and maintainability.',
            },
            {
                'title': 'Database Optimization',
                'description': 'Optimized PostgreSQL queries reducing response time by 40% using indexing and query optimization.',
            },
            {
                'title': 'Payment Integration',
                'description': 'Seamlessly integrated Razor Pay for secure payment processing with webhook handling.',
            },
            {
                'title': 'API Development',
                'description': 'Developed 400+ REST API endpoints and thoroughly tested them using Postman for request validation and response verification.',
            },
        ],
        'challenges_solutions': [
            {
                'challenge': 'Managing complex role-based permissions across multiple modules',
                'solution': 'Implemented custom permission classes and middleware for granular access control',
            },
            {
                'challenge': 'Handling large datasets for financial reporting',
                'solution': 'Utilized Django ORM optimization, select_related, prefetch_related, and database indexing',
            },
        ],
        'outcomes': [
            'Reduced manual cost tracking time by 70%',
            'Improved billing accuracy to 99.8%',
            'Enabled real-time financial insights for management',
            'Achieved seamless integration with frontend applications',
        ],
    },
    'alliance-crm': {
        'id': 'alliance-crm',
        'title': 'Alliance CRM',
        'subtitle': 'College Management & Student Application System',
        'description': 'Scalable college management system for handling student applications, coupon-based payments, and lead tracking with secure role-based access.',
        'technologies': ['Django REST', 'PostgreSQL', 'HDFC Payment Gateway', 'JWT'],
        'icon': 'fas fa-graduation-cap',
        'period': 'Jun 2025 - present',
        'status': 'In Progress',
        'role': 'Backend Developer',
        'team_size': '5 members',
        'full_description': '''
            Alliance CRM is a comprehensive college management system designed to streamline student 
            admissions, application processing, and financial transactions. The system handles thousands 
            of student applications with integrated payment processing and lead management capabilities.
        ''',
        'key_features': [
            'Student application and admission management',
            'Coupon-based discount and payment system',
            'Implemented lead tracking and conversion workflows using 300+ REST APIs and 150+ data models.',
            'Implemented HDFC Payment Gateway integration with webhook-based response handling.',
            'Implemented a document upload and verification system with Level 1 and Level 2 verification workflows.',
            'Built email and SMS notifications with scheduled, bulk emails and SendGrid–SES fallback.',
            'Implemented custom filters, Django default filters, and advanced filtering logic using Django ORM and Django REST Framework.',
            'Developed Python scripts for bulk uploading country, nationality, and 15K+ lead data from Excel files.',
        ],
        'technical_highlights': [
            {
                'title': 'Payment Integration',
                'description': 'Integrated HDFC Payment Gateway with webhook handling for secure transactions.',
            },
            {
                'title': 'Scalability',
                'description': 'Architected system to handle 10,000+ concurrent student applications during admission season.',
            },
            {
                'title': 'Security',
                'description': 'Implemented JWT authentication with refresh tokens and role-based access control.',
            },
            {
                'title': 'Data Management',
                'description': 'Designed efficient database models with proper relationships for student lifecycle tracking.',
            },
        ],
        'challenges_solutions': [
            {
                'challenge': 'High traffic during admission season causing performance issues',
                'solution': 'Implemented Redis caching, database connection pooling, and load balancing',
            },
            {
                'challenge': 'Complex coupon validation logic with multiple conditions',
                'solution': 'Created flexible coupon engine with rule-based validation system',
            },
        ],
        'outcomes': [
            'Successfully processed 15,000+ applications in first season',
            'Reduced application processing time by 60%',
            'Achieved 99.5% payment success rate',
            'Enhanced lead conversion rates by 25%',
        ],
    },
}

def home(request):
    """Render the main portfolio page"""
    context = {
        'nav_items': [
            {'id': 'home', 'name': 'Home', 'href': '#home'},
            {'id': 'about', 'name': 'About', 'href': '#about'},
            {'id': 'experience', 'name': 'Experience', 'href': '#experience'},
            {'id': 'projects', 'name': 'Projects', 'href': '#projects'},
            {'id': 'skills', 'name': 'Skills', 'href': '#skills'},
            {'id': 'contact', 'name': 'Contact', 'href': '#contact'},
        ],
        'roles': [
            'Django REST API Developer',
            'Backend Developer',
            'Python Developer',
        ],
        'skills': [
            {'name': 'Python & Django', 'level': 80},
            {'name': 'REST API Development', 'level': 90},
            {'name': 'PostgreSQL & MySQL', 'level': 85},
            {'name': 'Javascript & Vue.js', 'level': 30},
            {'name': 'Git & Version Control', 'level': 80},
        ],
        'projects': [
            {
                'id': proj['id'],
                'title': proj['title'],
                'description': proj['description'],
                'technologies': proj['technologies'],
                'icon': proj['icon'],
                'period': proj['period'],
            }
            for proj in PROJECTS_DATA.values()
        ],
        'skill_categories': [
            {
                'title': 'Backend',
                'icon': 'fas fa-server',
                'skills': ['Python3', 'Django REST Framework', 'Django', 'PostgreSQL', 'MySQL'],
            },
            {
                'title': 'Frontend',
                'icon': 'fas fa-palette',
                'skills': ['Tailwind CSS', 'HTML & CSS', 'JavaScript(Basic)', 'Vue.js(Basic)'],
            },
            {
                'title': 'Tools & Platforms',
                'icon': 'fas fa-tools',
                'skills': ['VS Code', 'Postman', 'GitLab', 'GitHub'],
            },
            {
                'title': 'Operating Systems',
                'icon': 'fas fa-desktop',
                'skills': ['Fedora Linux', 'Windows', 'Command Line'],
            },
        ],
    }
    return render(request, 'portfolio/home.html', context)

def project_detail(request, project_id):
    """Render individual project detail page"""
    project = PROJECTS_DATA.get(project_id)
    
    if not project:
        # Redirect to home page if project not found
        from django.shortcuts import redirect
        return redirect('home')
    
    context = {
        'project': project,
        'nav_items': [
            {'id': 'home', 'name': 'Home', 'href': '/'},
        ],
    }
    return render(request, 'portfolio/project_detail.html', context)

@require_http_methods(["POST"])
def contact(request):
    """Handle contact form submission"""
    try:
        data = json.loads(request.body)
        name = data.get('name', '')
        email = data.get('email', '')
        message = data.get('message', '')
        
        if not all([name, email, message]):
            return JsonResponse({
                'status': 'error',
                'message': 'All fields are required'
            }, status=400)
        
        # Send email (configure email settings in settings.py)
        subject = f'Portfolio Contact from {name}'
        email_message = f'From: {name}\nEmail: {email}\n\nMessage:\n{message}'
        
        send_mail(
            subject,
            email_message,
            settings.EMAIL_HOST_USER,
            ['keerthideveloper11@gmail.com'],
            fail_silently=False,
        )
        
        # For development, just print to console
        print(f"\n{'='*50}")
        print(f"Contact Form Submission")
        print(f"{'='*50}")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Message: {message}")
        print(f"{'='*50}\n")
        
        return JsonResponse({
            'status': 'success',
            'message': 'Thank you for your message! I\'ll get back to you soon.'
        })
        
    except json.JSONDecodeError:
        return JsonResponse({
            'status': 'error',
            'message': 'Invalid JSON data'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500)