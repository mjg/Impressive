##### STOCK SHADERS ############################################################

class SimpleQuad(object):
    "vertex buffer singleton for a simple quad (used by various shaders)"
    vbuf = None
    @classmethod
    def draw(self):
        gl.set_enabled_attribs(0)
        if not self.vbuf:
            self.vbuf = gl.GenBuffers()
            gl.BindBuffer(gl.ARRAY_BUFFER, self.vbuf)
            gl.BufferData(gl.ARRAY_BUFFER, data=[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0])
        else:
            gl.BindBuffer(gl.ARRAY_BUFFER, self.vbuf)
        gl.VertexAttribPointer(0, 4, gl.FLOAT, False, 0, 0)
        gl.DrawArrays(gl.TRIANGLE_STRIP, 0, 4)


class TexturedRectShader(GLShader):
    vs = """
        attribute highp vec4 aPosAndTexCoord;
        uniform highp vec4 uPosTransform;
        uniform highp vec4 uScreenTransform;
        uniform highp vec4 uTexTransform;
        varying mediump vec2 vTexCoord;
        void main() {
            highp vec2 pos = uPosTransform.xy + aPosAndTexCoord.xy * uPosTransform.zw;
            gl_Position = vec4(uScreenTransform.xy + pos * uScreenTransform.zw, 0.0, 1.0);
            vTexCoord = uTexTransform.xy + aPosAndTexCoord.zw * uTexTransform.zw;
        }
    """
    fs = """
        uniform lowp vec4 uColor;
        uniform lowp sampler2D uTex;
        varying mediump vec2 vTexCoord;
        void main() {
            gl_FragColor = uColor * texture2D(uTex, vTexCoord);
        }
    """
    attributes = { 0: 'aPosAndTexCoord' }
    uniforms = ['uPosTransform', 'uScreenTransform', 'uTexTransform', 'uColor']

    def draw(self, x0, y0, x1, y1, s0=0.0, t0=0.0, s1=1.0, t1=1.0, tex=None, color=1.0):
        self.use()
        if tex:
            gl.BindTexture(gl.TEXTURE_2D, tex)
        if isinstance(color, float):
            gl.Uniform4f(self.uColor, color, color, color, 1.0)
        else:
            gl.Uniform(self.uColor, color)
        gl.Uniform(self.uPosTransform, x0, y0, x1 - x0, y1 - y0)
        gl.Uniform(self.uScreenTransform, ScreenTransform)
        gl.Uniform(self.uTexTransform, s0, t0, s1 - s0, t1 - t0)
        SimpleQuad.draw()
RequiredShaders.append(TexturedRectShader)


class BlurShader(GLShader):
    vs = """
        attribute highp vec2 aPos;
        uniform highp vec4 uScreenTransform;
        varying mediump vec2 vTexCoord;
        void main() {
            gl_Position = vec4(uScreenTransform.xy + aPos * uScreenTransform.zw, 0.0, 1.0);
            vTexCoord = aPos;
        }
    """
    fs = """
        uniform lowp float uIntensity;
        uniform mediump sampler2D uTex;
        uniform mediump vec2 uDeltaTexCoord;
        varying mediump vec2 vTexCoord;
        void main() {
            gl_FragColor = vec4(uIntensity, uIntensity, uIntensity, 0.125) * (
                texture2D(uTex, vTexCoord)
              + texture2D(uTex, vTexCoord + uDeltaTexCoord * vec2(+0.71, +0.71))
              + texture2D(uTex, vTexCoord + uDeltaTexCoord * vec2(+0.99, -0.11))
              + texture2D(uTex, vTexCoord + uDeltaTexCoord * vec2(+0.53, -0.85))
              + texture2D(uTex, vTexCoord + uDeltaTexCoord * vec2(-0.33, -0.94))
              + texture2D(uTex, vTexCoord + uDeltaTexCoord * vec2(-0.94, -0.33))
              + texture2D(uTex, vTexCoord + uDeltaTexCoord * vec2(-0.85, +0.53))
              + texture2D(uTex, vTexCoord + uDeltaTexCoord * vec2(-0.11, +0.99))
            );
        }
    """
    attributes = { 0: 'aPos' }
    uniforms = ['uScreenTransform', 'uDeltaTexCoord', 'uIntensity']

    def draw(self, dtx, dty, intensity=1.0, tex=None):
        self.use()
        if tex:
            gl.BindTexture(gl.TEXTURE_2D, tex)
        gl.Uniform(self.uScreenTransform, ScreenTransform)
        gl.Uniform2f(self.uDeltaTexCoord, dtx, dty)
        gl.Uniform1f(self.uIntensity, intensity * 0.125)
        SimpleQuad.draw()
RequiredShaders.append(BlurShader)


class ProgressBarShader(GLShader):
    vs = """
        attribute highp vec2 aPos;
        uniform highp vec4 uPosTransform;
        uniform lowp vec4 uColor0;
        uniform lowp vec4 uColor1;
        varying lowp vec4 vColor;
        void main() {
            gl_Position = vec4(uPosTransform.xy + aPos * uPosTransform.zw, 0.0, 1.0);
            vColor = mix(uColor0, uColor1, aPos.y);
        }
    """
    fs = """
        varying lowp vec4 vColor;
        void main() {
            gl_FragColor = vColor;
        }
    """
    attributes = { 0: 'aPos' }
    uniforms = ['uPosTransform', 'uColor0', 'uColor1']

    def draw(self, x0, y0, x1, y1, color0, color1):
        self.use()
        tx0 = ScreenTransform[0] + ScreenTransform[2] * x0
        ty0 = ScreenTransform[1] + ScreenTransform[3] * y0
        tx1 = ScreenTransform[0] + ScreenTransform[2] * x1
        ty1 = ScreenTransform[1] + ScreenTransform[3] * y1
        gl.Uniform4f(self.uPosTransform, tx0, ty0, tx1 - tx0, ty1 - ty0)
        gl.Uniform(self.uColor0, color0)
        gl.Uniform(self.uColor1, color1)
        SimpleQuad.draw()
RequiredShaders.append(ProgressBarShader)
