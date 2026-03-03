'use client';

const STORAGE_KEY = 'merit-capital-sharing-token';
const ACTIVATION_TOKEN_KEY = 'merit-capital-activation-token';

/**
 * Set sharing token in sessionStorage
 */
export function setSharingToken(token: string): void {
  if (typeof window !== 'undefined') {
    try {
      sessionStorage.setItem(STORAGE_KEY, token);
    } catch (error) {
      console.error('Failed to store sharing token:', error);
    }
  }
}

/**
 * Get sharing token from URL param, cookie, or sessionStorage
 */
export function getSharingToken(): string | null {
  if (typeof window === 'undefined') return null;
  
  // First check URL params
  const urlParams = new URLSearchParams(window.location.search);
  const urlToken = urlParams.get('shared-by');
  if (urlToken) {
    // Store it for fallback
    setSharingToken(urlToken);
    return urlToken;
  }
  
  // Check cookie (set by server)
  try {
    const cookies = document.cookie.split(';');
    const cookieToken = cookies
      .find(c => c.trim().startsWith(`${STORAGE_KEY}=`))
      ?.split('=')[1]
      ?.trim();
    
    if (cookieToken) {
      // Sync to sessionStorage
      setSharingToken(cookieToken);
      return cookieToken;
    }
  } catch (error) {
    // Cookie reading failed, continue to sessionStorage
  }
  
  // Fallback to sessionStorage
  try {
    return sessionStorage.getItem(STORAGE_KEY);
  } catch (error) {
    console.error('Failed to read sharing token:', error);
    return null;
  }
}

/**
 * Clear sharing token from sessionStorage
 */
export function clearSharingToken(): void {
  if (typeof window !== 'undefined') {
    try {
      sessionStorage.removeItem(STORAGE_KEY);
    } catch (error) {
      console.error('Failed to clear sharing token:', error);
    }
  }
}

/**
 * Set activation token in sessionStorage
 */
export function setActivationToken(token: string): void {
  if (typeof window !== 'undefined') {
    try {
      sessionStorage.setItem(ACTIVATION_TOKEN_KEY, token);
    } catch (error) {
      console.error('Failed to store activation token:', error);
    }
  }
}/**
 * Get activation token from sessionStorage, cookie (for migration), or URL params
 */
export function getActivationToken(): string | null {
  if (typeof window === 'undefined') return null;
  
  // First check sessionStorage
  try {
    const sessionToken = sessionStorage.getItem(ACTIVATION_TOKEN_KEY);
    if (sessionToken) {
      return sessionToken;
    }
  } catch (error) {
    // SessionStorage read failed, continue to cookie check
  }
  
  // Check cookie (for migration from server-set cookie)
  try {
    const cookies = document.cookie.split(';');
    const cookieToken = cookies
      .find(c => c.trim().startsWith(`${ACTIVATION_TOKEN_KEY}=`))
      ?.split('=')[1]
      ?.trim();
    
    if (cookieToken) {
      // Migrate from cookie to sessionStorage
      setActivationToken(cookieToken);
      // Clear cookie
      document.cookie = `${ACTIVATION_TOKEN_KEY}=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;`;
      return cookieToken;
    }
  } catch (error) {
    // Cookie reading failed
  }
  
  return null;
}

/**
 * Clear activation token from sessionStorage
 */
export function clearActivationToken(): void {
  if (typeof window !== 'undefined') {
    try {
      sessionStorage.removeItem(ACTIVATION_TOKEN_KEY);
      // Also clear cookie if it exists
      document.cookie = `${ACTIVATION_TOKEN_KEY}=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;`;
    } catch (error) {
      console.error('Failed to clear activation token:', error);
    }
  }
}