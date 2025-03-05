INTRODUCTION

1. First steps

	•	Explicación: Configuración inicial del proyecto NestJS usando el CLI. Se crean controladores, módulos y
	servicios como base del proyecto.

```bash
npm install -g @nestjs/cli
nest new my-app
```

Controlador básico:
```javascript
@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World!';
  }
}
```


OVERVIEW

2. Controllers

	•	Explicación: Manejan rutas y peticiones HTTP entrantes. Se implementan con decoradores como @Controller y @Get.

```javascript
@Controller('users')
export class UsersController {
  @Get()
  findAll(): string {
    return 'List of users';
  }
}
```


3. Providers

	•	Explicación: Clases que encapsulan lógica empresarial. Pueden ser servicios, repositorios, etc. Usan
	@Injectable.

```javascript
@Injectable()
export class UsersService {
  findAll(): string[] {
    return ['Alice', 'Bob'];
  }
}
```


4. Modules

	•	Explicación: Agrupan lógica relacionada como controladores, servicios y otros módulos. Todos los proyectos
	tienen al menos un módulo raíz.

```javascript
@Module({
  controllers: [UsersController],
  providers: [UsersService],
})
export class UsersModule {}
```


5. Middleware

	•	Explicación: Procesan peticiones antes de que lleguen a los controladores. Útiles para autenticación, logging,
	etc.

```javascript
export class LoggerMiddleware implements NestMiddleware {
  use(req: Request, res: Response, next: () => void) {
    console.log(`Request...`);
    next();
  }
}
```


6. Exception filters

	•	Explicación: Manejan errores de manera centralizada y personalizada.

```javascript
@Catch(HttpException)
export class HttpExceptionFilter implements ExceptionFilter {
  catch(exception: HttpException, host: ArgumentsHost) {
    const ctx = host.switchToHttp();
    const response = ctx.getResponse();
    const status = exception.getStatus();
    response.status(status).json({ message: exception.message });
  }
}
```


7. Pipes

	•	Explicación: Transforman o validan datos antes de que lleguen a los controladores.

```javascript
@Controller()
export class AppController {
  @Post()
  create(@Body(new ValidationPipe()) createDto: CreateDto) {
    return createDto;
  }
}
```


8. Guards

	•	Explicación: Implementan lógica de autorización para rutas o controladores.

```javascript
@Injectable()
export class AuthGuard implements CanActivate {
  canActivate(context: ExecutionContext): boolean {
    const request = context.switchToHttp().getRequest();
    return request.headers.authorization === 'valid_token';
  }
}
```

9. Interceptors

	•	Explicación: Manipulan peticiones y respuestas antes o después de procesarlas.

```javascript
@Injectable()
export class TransformInterceptor implements NestInterceptor {
  intercept(context: ExecutionContext, next: CallHandler): Observable<any> {
    return next.handle().pipe(map(data => ({ result: data })));
  }
}
```


10. Custom decorators

	•	Explicación: Permiten crear decoradores personalizados para simplificar lógica.

```javascript
export const User = createParamDecorator(
  (data: string, ctx: ExecutionContext) => {
    const request = ctx.switchToHttp().getRequest();
    return request.user;
  },
);
```


FUNDAMENTALS

11. Custom providers

	•	Explicación: Proveedores personalizados con lógica avanzada.

```javascript
const customProvider = {
  provide: 'TOKEN',
  useValue: 'Custom Value',
};
```


12. Asynchronous providers

	•	Explicación: Proveedores que manejan lógica asíncrona.

```javascript
const asyncProvider = {
  provide: 'ASYNC_VALUE',
  useFactory: async () => await fetchData(),
};
```


13. Dynamic modules

	•	Explicación: Permiten crear módulos configurables.

```javascript
@Module({})
export class DynamicModule {
  static forRoot(config: any): DynamicModule {
    return {
      module: DynamicModule,
      providers: [{ provide: 'CONFIG', useValue: config }],
    };
  }
}
```


14. Injection scopes

	•	Explicación: Controlan el ciclo de vida de las dependencias.

```javascript
@Injectable({ scope: Scope.REQUEST })
export class ScopedService {}
```


15. Circular dependency

	•	Explicación: Resolver dependencias circulares mediante forwardRef.

```javascript
@Injectable()
export class AService {
  constructor(@Inject(forwardRef(() => BService)) private bService: BService) {}
}
```


16. Module reference

	•	Explicación: Permite acceder dinámicamente a módulos.

```javascript
constructor(private moduleRef: ModuleRef) {}
```


17. Lazy-loading modules

	•	Explicación: Carga diferida de módulos para optimizar recursos.

```javascript
const LazyModule = await import('./lazy/lazy.module').then(m => m.LazyModule);
```


18. Execution context

	•	Explicación: Detalles sobre el contexto actual (HTTP, WebSocket, etc.).

```javascript
const context = host.switchToHttp();
```


19. Lifecycle events

	•	Explicación: Hooks para eventos del ciclo de vida del módulo.

```javascript
@Injectable()
export class AppService implements OnModuleInit {
  onModuleInit() {
    console.log('Module Initialized');
  }
}
```


20. Platform agnosticism

	•	Explicación: Funciona en múltiples plataformas como Express o Fastify.

```javascript
const app = await NestFactory.create(AppModule, new FastifyAdapter());
```


21. Testing

	•	Explicación: Herramientas como Jest para pruebas unitarias e integración.

```javascript
describe('AppController', () => {
  it('should return "Hello World"', () => {
    expect(controller.getHello()).toBe('Hello World');
  });
});
```


TECHNIQUES

22. Configuration

	•	Explicación: Manejo de variables de entorno y configuración global de la aplicación.

```javascript
@Module({
  imports: [ConfigModule.forRoot()],
})
export class AppModule {}

@Injectable()
export class ConfigService {
  constructor(private configService: ConfigService) {}
  get(key: string): string {
    return this.configService.get(key);
  }
}
```


23. Database

	•	Explicación: Integración con bases de datos relacionales y no relacionales usando bibliotecas como TypeORM o
	Sequelize.

```javascript
@Entity()
export class User {
  @PrimaryGeneratedColumn()
  id: number;

  @Column()
  name: string;
}

@Injectable()
export class UserService {
  constructor(
    @InjectRepository(User)
    private userRepository: Repository<User>,
  ) {}

  findAll(): Promise<User[]> {
    return this.userRepository.find();
  }
}
```


24. Mongo

	•	Explicación: Soporte para MongoDB mediante Mongoose o MongoDB Driver.

```javascript
@Schema()
export class User {
  @Prop()
  name: string;
}

const UserSchema = SchemaFactory.createForClass(User);

@Injectable()
export class UserService {
  constructor(@InjectModel('User') private userModel: Model<User>) {}

  async findAll(): Promise<User[]> {
    return this.userModel.find().exec();
  }
}
```


25. Validation

	•	Explicación: Validación de datos usando decoradores y clases.

```javascript
export class CreateUserDto {
  @IsString()
  @Length(3, 20)
  name: string;

  @IsEmail()
  email: string;
}

@Post()
create(@Body(new ValidationPipe()) createUserDto: CreateUserDto) {
  return this.userService.create(createUserDto);
}
```


26. Caching

	•	Explicación: Mejora del rendimiento mediante caché (en memoria o distribuidos como Redis).

```javascript
@Cacheable()
findAll(): Promise<string[]> {
  return ['cachedData1', 'cachedData2'];
}
```


27. Serialization

	•	Explicación: Transformación y filtrado de datos de salida.

```javascript
export class UserResponse {
  @Expose()
  name: string;

  @Exclude()
  password: string;
}

@UseInterceptors(ClassSerializerInterceptor)
findAll(): UserResponse[] {
  return users;
}
```


28. Versioning

	•	Explicación: Gestión de versiones de la API.

```javascript
const app = await NestFactory.create(AppModule);
app.enableVersioning({ type: VersioningType.URI });
```


29. Task scheduling

	•	Explicación: Automatización de tareas repetitivas o programadas.

```javascript
@Injectable()
export class TaskService {
  @Cron('45 * * * * *')
  handleCron() {
    console.log('Called at 45th second of every minute');
  }
}
```


30. Queues

	•	Explicación: Manejo de tareas en cola mediante Redis o RabbitMQ.

```javascript
@Processor('emails')
export class EmailProcessor {
  @Process('send-email')
  async sendEmail(job: Job<any>) {
    console.log(`Sending email to ${job.data.email}`);
  }
}
```


31. Logging

	•	Explicación: Registro de información y errores en la aplicación.

```javascript
const logger = new Logger('AppService');
logger.log('Application started');
```


32. Cookies

	•	Explicación: Gestión de cookies para sesiones o datos temporales.

```javascript
@Get('cookies')
getCookies(@Req() request: Request): string {
  return request.cookies['key'];
}
```


33. Events

	•	Explicación: Sistema de eventos para comunicación interna entre componentes.

```javascript
@Injectable()
export class EventService {
  @OnEvent('user.created')
  handleUserCreatedEvent(payload: UserCreatedEvent) {
    console.log('User created event received', payload);
  }
}
```


34. Compression

	•	Explicación: Compresión de respuestas HTTP para optimizar ancho de banda.

```javascript
const app = await NestFactory.create(AppModule, { compression: true });
```


35. File upload

	•	Explicación: Manejo de subida de archivos.

```javascript
@Post('upload')
@UseInterceptors(FileInterceptor('file'))
uploadFile(@UploadedFile() file: Express.Multer.File) {
  console.log(file);
}
```


36. Streaming files

	•	Explicación: Transmisión de archivos grandes.

```javascript
@Get('stream')
streamFile(@Res() res: Response) {
  const file = createReadStream('./largeFile.mp4');
  file.pipe(res);
}
```


37. HTTP module

	•	Explicación: Realización de solicitudes HTTP externas.

```javascript
@Injectable()
export class HttpService {
  constructor(private httpService: HttpModule) {}

  fetchData() {
    return this.httpService.get('https://api.example.com');
  }
}
```


38. Session

	•	Explicación: Manejo de sesiones de usuario.

```javascript
import * as session from 'express-session';
app.use(session({ secret: 'mySecret', resave: false, saveUninitialized: false }));
```


39. Model-View-Controller (MVC)

	•	Explicación: Implementación del patrón MVC.

```javascript
@Controller('home')
export class HomeController {
  @Get()
  renderHome(@Res() res: Response) {
    res.render('index', { title: 'Home Page' });
  }
}
```


40. Performance (Fastify)

	•	Explicación: Optimización del rendimiento utilizando Fastify.

```javascript
const app = await NestFactory.create(AppModule, new FastifyAdapter());
```


41. Server-Sent Events

	•	Explicación: Comunicación en tiempo real desde el servidor al cliente.

```javascript
@Get('sse')
@Sse()
sendEvents(): Observable<MessageEvent> {
  return interval(1000).pipe(map(() => ({ data: { time: new Date().toISOString() } })));
}
```

