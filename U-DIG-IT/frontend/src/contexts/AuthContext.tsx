import { createContext, useCallback, useContext, useEffect, useMemo, useState, type ReactNode } from 'react'
import { useQueryClient } from '@tanstack/react-query'

import { fetchCurrentUser, login as loginRequest, register as registerRequest } from '../api/endpoints'
import { setAccessToken } from '../api/client'
import type { AuthUser } from '../types'

interface AuthContextValue {
  user: AuthUser | null
  token: string | null
  isAuthenticated: boolean
  loading: boolean
  login: (email: string, password: string) => Promise<void>
  register: (payload: { email: string; fullName: string; password: string; phoneNumber?: string; companyName?: string }) => Promise<void>
  logout: () => void
}

const AuthContext = createContext<AuthContextValue | undefined>(undefined)

const ACCESS_TOKEN_STORAGE_KEY = 'udigit.access_token'

interface AuthProviderProps {
  children: ReactNode
}

export const AuthProvider = ({ children }: AuthProviderProps) => {
  const queryClient = useQueryClient()
  const [user, setUser] = useState<AuthUser | null>(null)
  const [token, setToken] = useState<string | null>(() => localStorage.getItem(ACCESS_TOKEN_STORAGE_KEY))
  const [loading, setLoading] = useState<boolean>(Boolean(token))

  const loadSession = useCallback(async () => {
    if (!token) {
      setLoading(false)
      return
    }

    try {
      setAccessToken(token)
      const profile = await fetchCurrentUser()
      setUser(profile)
    } catch (error) {
      console.error('Unable to load session', error)
      setUser(null)
      setToken(null)
      localStorage.removeItem(ACCESS_TOKEN_STORAGE_KEY)
      setAccessToken(null)
    } finally {
      setLoading(false)
    }
  }, [token])

  useEffect(() => {
    void loadSession()
  }, [loadSession])

  const persistToken = useCallback((value: string | null) => {
    setToken(value)
    setAccessToken(value)
    if (value) {
      localStorage.setItem(ACCESS_TOKEN_STORAGE_KEY, value)
    } else {
      localStorage.removeItem(ACCESS_TOKEN_STORAGE_KEY)
    }
  }, [])

  const login = useCallback(
    async (email: string, password: string) => {
      const { accessToken } = await loginRequest(email, password)
      persistToken(accessToken)
      const profile = await fetchCurrentUser()
      setUser(profile)
    },
    [persistToken],
  )

  const register = useCallback(
    async (payload: { email: string; fullName: string; password: string; phoneNumber?: string; companyName?: string }) => {
      const { accessToken } = await registerRequest(payload)
      persistToken(accessToken)
      const profile = await fetchCurrentUser()
      setUser(profile)
    },
    [persistToken],
  )

  const logout = useCallback(() => {
    persistToken(null)
    setUser(null)
    queryClient.clear()
  }, [persistToken, queryClient])

  const value = useMemo(
    () => ({ user, token, isAuthenticated: Boolean(user && token), login, register, logout, loading }),
    [user, token, login, register, logout, loading],
  )

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>
}

export const useAuthContext = () => {
  const context = useContext(AuthContext)
  if (!context) {
    throw new Error('useAuthContext must be used within an AuthProvider')
  }
  return context
}
