# Social Media API - User Follows and Feed Functionality

## Overview

This project extends the Social Media API with user follow relationships and a dynamic feed system. Users can now follow other users and view an aggregated feed of posts from their network, mimicking core functionalities of popular social media platforms.

## Features

- **User Following System**: Users can follow and unfollow other users through dedicated API endpoints
- **Dynamic Feed**: View an aggregated, chronologically-ordered feed of posts from users you follow
- **Permission Management**: Secure endpoints that ensure users can only modify their own following list
- **Self-Referential Relationships**: Efficient many-to-many relationship structure on the User model

## Models

### User Model

The custom User model has been updated to include a `following` field that represents a many-to-many relationship to itself:

```python
class CustomUser(AbstractUser):
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='followers',
        blank=True
    )
```

**Migrations**: Run the following commands to apply database changes:

```bash
python manage.py makemigrations accounts
python manage.py migrate
```

## API Endpoints

### Follow Management

#### Follow a User
- **Endpoint**: `POST /api/accounts/follow/<int:user_id>/`
- **Authentication**: Required (Bearer Token)
- **Description**: Add a user to your following list
- **Request Body**: None
- **Response** (200 OK):
```json
{
    "message": "Successfully followed user",
    "following_id": 2
}
```
- **Status Codes**: 
  - `200 OK`: Successfully followed
  - `400 Bad Request`: Already following or invalid user
  - `401 Unauthorized`: Authentication required
  - `404 Not Found`: User not found

#### Unfollow a User
- **Endpoint**: `DELETE /api/accounts/unfollow/<int:user_id>/`
- **Authentication**: Required (Bearer Token)
- **Description**: Remove a user from your following list
- **Response** (200 OK):
```json
{
    "message": "Successfully unfollowed user",
    "unfollowed_id": 2
}
```
- **Status Codes**: 
  - `200 OK`: Successfully unfollowed
  - `400 Bad Request`: Not following this user
  - `401 Unauthorized`: Authentication required
  - `404 Not Found`: User not found

### Feed Management

#### Get User Feed
- **Endpoint**: `GET /api/posts/feed/`
- **Authentication**: Required (Bearer Token)
- **Description**: Retrieve posts from all users you follow, ordered by creation date (newest first)
- **Query Parameters**:
  - `page` (optional): Page number for pagination (default: 1)
  - `page_size` (optional): Posts per page (default: 10)
- **Response** (200 OK):
```json
{
    "count": 25,
    "next": "http://api.example.com/posts/feed/?page=2",
    "previous": null,
    "results": [
        {
            "id": 15,
            "title": "Amazing Day",
            "content": "Just finished a great project!",
            "author": "john_doe",
            "created_at": "2024-01-15T10:30:00Z",
            "updated_at": "2024-01-15T10:30:00Z"
        },
        {
            "id": 14,
            "title": "Django Tips",
            "content": "Here are some useful Django patterns...",
            "author": "jane_smith",
            "created_at": "2024-01-14T15:45:00Z",
            "updated_at": "2024-01-14T15:45:00Z"
        }
    ]
}
```
- **Status Codes**: 
  - `200 OK`: Feed retrieved successfully
  - `401 Unauthorized`: Authentication required
  - `404 Not Found`: Feed not found

## URL Configuration

### accounts/urls.py
```python
from django.urls import path
from . import views

urlpatterns = [
    path('follow/<int:user_id>/', views.follow_user, name='follow_user'),
    path('unfollow/<int:user_id>/', views.unfollow_user, name='unfollow_user'),
]
```

### posts/urls.py
```python
from django.urls import path
from . import views

urlpatterns = [
    path('feed/', views.user_feed, name='user_feed'),
]
```

## Views Implementation

### Follow Management Views (accounts/views.py)

```python
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import CustomUser

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_user(request, user_id):
    user_to_follow = get_object_or_404(CustomUser, id=user_id)
    
    if user_to_follow == request.user:
        return Response(
            {"error": "You cannot follow yourself"},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    if request.user.following.filter(id=user_id).exists():
        return Response(
            {"error": "You are already following this user"},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    request.user.following.add(user_to_follow)
    return Response(
        {"message": "Successfully followed user", "following_id": user_id},
        status=status.HTTP_200_OK
    )

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def unfollow_user(request, user_id):
    user_to_unfollow = get_object_or_404(CustomUser, id=user_id)
    
    if not request.user.following.filter(id=user_id).exists():
        return Response(
            {"error": "You are not following this user"},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    request.user.following.remove(user_to_unfollow)
    return Response(
        {"message": "Successfully unfollowed user", "unfollowed_id": user_id},
        status=status.HTTP_200_OK
    )
```

### Feed View (posts/views.py)

```python
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import Post
from .serializers import PostSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_feed(request):
    following_users = request.user.following.all()
    posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
    
    paginator = PageNumberPagination()
    paginator.page_size = 10
    paginated_posts = paginator.paginate_queryset(posts, request)
    
    serializer = PostSerializer(paginated_posts, many=True)
    return paginator.get_paginated_response(serializer.data)
```

## Testing

### Using Postman

1. **Authenticate**: Obtain a token via the login endpoint
2. **Follow User**: Send `POST` request to `/api/accounts/follow/2/` with Bearer token
3. **View Feed**: Send `GET` request to `/api/posts/feed/` with Bearer token
4. **Unfollow User**: Send `DELETE` request to `/api/accounts/unfollow/2/` with Bearer token

### Using cURL

```bash
# Follow a user
curl -X POST http://localhost:8000/api/accounts/follow/2/ \
  -H "Authorization: Bearer YOUR_TOKEN"

# Get feed
curl -X GET http://localhost:8000/api/posts/feed/ \
  -H "Authorization: Bearer YOUR_TOKEN"

# Unfollow a user
curl -X DELETE http://localhost:8000/api/accounts/unfollow/2/ \
  -H "Authorization: Bearer YOUR_TOKEN"
```

## Validation Rules

- Users cannot follow themselves
- Duplicate follows are prevented
- Only authenticated users can follow/unfollow or access feeds
- Users can only modify their own following list
- Empty feeds are allowed for users not following anyone

## Error Handling

All endpoints include comprehensive error handling with appropriate HTTP status codes and descriptive error messages. Common errors include:

- `400 Bad Request`: Invalid operations (self-follow, duplicate follow)
- `401 Unauthorized`: Missing or invalid authentication
- `404 Not Found`: User or resource not found
- `403 Forbidden`: Insufficient permissions

## Future Enhancements

- Mutual follow notifications
- Follow suggestions based on user activity
- Follow request workflow (public/private accounts)
- Feed filtering and sorting options
- Follow statistics and analytics

## Contributing

When extending this functionality, ensure all new features include:
- Proper permission checks
- Comprehensive error handling
- Unit and integration tests
- Updated API documentation