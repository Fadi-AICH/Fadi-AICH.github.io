export async function onRequestGet(context) {
  const clientId = context.env.GITHUB_CLIENT_ID;
  const siteURL = new URL(context.request.url).origin;
  const redirectURI = `${siteURL}/callback`;
  const authURL = `https://github.com/login/oauth/authorize?client_id=${clientId}&redirect_uri=${encodeURIComponent(redirectURI)}&scope=repo,user`;
  return Response.redirect(authURL, 302);
}
